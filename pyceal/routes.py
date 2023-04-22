from flask import render_template , url_for, request, flash, redirect, g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from pyceal import app, db
from pyceal.forms import ID_Form, LoginForm
from pyceal.models import User
from pyceal.generate_id import Generate_ID
from werkzeug.utils import secure_filename
import base64



@app.route("/")
@app.route("/index")
def root_page():
    return render_template('root_page.html')

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

                sign_img_data = sign_img.read(),
                sign_img_name = sign_name,
                sign_img_mimetype = sign_mimetype,

            )
        
        db.session.add(user)
        db.session.commit()

        flash(f'ID Succesfully generated for {form.full_name.data}', 'success')
        
        return redirect (url_for('login')) ## change to preview page later
    
    return render_template ('id_generator.html', form=form)

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
    
    return render_template ('login.html', form=form)

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

    gen_id = Generate_ID(current_user)
    gen_id.prt_name()
    gen_id.make_id()

    return render_template ('preview.html', user=user, data=data)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    flash("You are currently not logged in.")
    return redirect(url_for('root_page'))