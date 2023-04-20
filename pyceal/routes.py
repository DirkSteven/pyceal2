from flask import render_template , url_for, request, flash, redirect, g
from pyceal import app
from pyceal.forms import ID_Form, LoginForm
from pyceal.models import User


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

