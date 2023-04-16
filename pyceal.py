from flask import Flask, render_template , url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import ID_Form, LoginForm


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '65dd8a8a9be421c2b8a4f3fdcc42f36a'
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     sr_code = db.Column (db.String(60), nullable=False)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}' )"


@app.route("/")
def root_page():
    return render_template ('root_page.html')

@app.route("/id_generator", methods=['GET', 'POST'])
def id_gen():
    form = ID_Form()
    # if form.validate_on_submit():
    #     flash(f'ID Succesfully generated for {form.full_name}', 'success')
    #     return redirect (url_for('login')) ## change to preview page later
    return render_template ('id_generator.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
     form = LoginForm()
     return render_template ('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)