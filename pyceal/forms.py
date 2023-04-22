from flask_wtf  import FlaskForm
from pyceal import app, db
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp
    

class ID_Form(FlaskForm):

    full_name = StringField('Full Name', validators=[DataRequired()])
    program = StringField('Program', validators=[DataRequired()])
    year_validity = StringField('Year', validators=[DataRequired()])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=8), Regexp('^[0-9-]+$')])
    email = StringField('Email', validators=[DataRequired(), Email()])

    id_img = FileField('Upload ID Picture', name='id_img', validators=[FileRequired()])
    sign_img = FileField('Upload Signature', name='sign_img', validators=[FileRequired()])

    contact_person = StringField('Contact in Person', validators=[DataRequired()])
    contact_number = StringField('Personal Contact Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])

    generate_id = SubmitField("Generate ID")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=10), Regexp('^[0-9-]+$')]) 
    remember_me = BooleanField("Remember Me")
    login = SubmitField('Login')

