from flask import render_template , url_for, request, flash, redirect, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from pyceal import app, db
from pyceal.forms import ID_Form, LoginForm, DecodeForm
from pyceal.models import User
from pyceal.generate_id import Generate_ID
from werkzeug.utils import secure_filename
import base64, io


@app.route("/")


@app.route("/index")
def root_page():
    return render_template('root_page.html', title="PyCeal | Secured ID Generator")


@app.route("/id_generator", methods=['GET', 'POST'])
def id_generator():
    form = ID_Form()

    if current_user.is_authenticated:

        return redirect(url_for('preview'))

    if form.validate_on_submit():

        id_img = request.files['id_img']
        id_name = secure_filename(id_img.filename)	
        id_mimetype = id_img.mimetype

        sign_img = request.files['sign_img']
        sign_name = secure_filename(sign_img.filename)	
        sign_mimetype = sign_img.mimetype
        
        gen_id = Generate_ID(current_user)

        image_bytes = io.BytesIO()
        sign_img = gen_id.create_sign_pic(sign_img.read()).convert('RGBA').save(image_bytes, format='PNG')
        sign_img = image_bytes.getvalue()

        user = User(
                full_name = form.full_name.data,
                program = form.program.data,
                email = form.email.data,
                sr_code = form.sr_code.data,
                year_validity = form.year_validity.data,

                contact_person = form.contact_person.data,
                address = form.address.data,
                contact_number = form.contact_number.data,

                id_img_data = id_img.read(),
                id_img_name = id_name,
                id_img_mimetype = id_mimetype,

                sign_img_data = sign_img,
                sign_img_name = sign_name,
                sign_img_mimetype = sign_mimetype,
            )
        
        db.session.add(user)
        db.session.commit()

        flash(f'ID Succesfully generated for {form.full_name.data}', 'success')
        
        return redirect (url_for('login')) 
    
    return render_template ('id_generator.html', form=form, title = "PyCeal | ID Generator")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:

        return redirect(url_for('preview'))
    
    form = LoginForm()

    if form.validate_on_submit():
		#search the database amd return the first result
        user = User.query.filter_by(email=form.email.data).first()

		#check if either no user was found or the password is incorrecr
        if user is None or not user.check_srcode(form.sr_code.data):
            flash('Invalid username or password')

            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

		#get the page the user was trying to access
        next_page = request.args.get('next')

		# check if next page exist or its netlocation is empty
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for('root_page')

        return redirect(next_page)
    
    return render_template ('login.html', form=form, title ="PyCeal | Log In")


@app.route('/decode', methods=['GET', 'POST'])
@login_required
def decode():
    form = DecodeForm()

    decoded_messsage = "No data was found."

    data = {
        "decoded_messsage": decoded_messsage,
    }

    if form.validate_on_submit():
        img_file = request.files['img_file']
        img_name = secure_filename(img_file.filename)  
        img_mimetype = img_file.mimetype

        print(img_file)

        img_data = img_file.read()
        display_image = base64.b64encode(img_data).decode('ascii')
        gen_id = Generate_ID(current_user)
        decoded_messsage = gen_id.decode_image(img_data, "NEU-BSU")

        validation_result = ""
        error_result = ""


        if decoded_messsage == gen_id.validation_message:
            validation_result = "**THIS IS A VALID BSU ID**"
        elif decoded_messsage == gen_id.error_message:
            error_result = decoded_messsage
            decoded_messsage = ""

        data["decoded_messsage"] = decoded_messsage
        data["validation_result"] = validation_result
        data["error_result"] = error_result
        data["selected_img"] = display_image

        return render_template('decode.html', title="Decoder", form=form, data=data)

    return render_template('decode.html', title="Decoder", form=form, data=data)



@app.route("/preview", methods=['GET', 'POST'])
@login_required
def preview():
    user = current_user
    if not user.is_authenticated:
        flash('You have yet to login to your account.')
    data = {
		"id_img": base64.b64encode(user.id_img_data).decode('utf-8'),
		"id_img_mimetype" : user.id_img_mimetype,

        "sign_img": base64.b64encode(user.sign_img_data).decode('utf-8'),
		"sign_img_mimetype" : user.sign_img_mimetype
	}

    gen_id = Generate_ID(user)
    gen_id.set_user_data()
    gen_id.make_id()

    return render_template ('preview.html', user=user, data=data, title="PyCeal | ID Generator")


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()

        return redirect(url_for('login'))
    flash("You are currently not logged in.")
    
    return redirect(url_for('root_page'))

@app.route('/download')
def download():
    # Get the filename of the image file
    filename = 'output_pic.png'

    # Use send_from_directory to send the file to the user's browser
    return send_from_directory(
        app.static_folder, 'images/user_images/' + filename, 
        as_attachment=True,
        )

@app.route("/modal")
def modal():
    return render_template("modal.html")
