from flask_wtf  import FlaskForm
from pyceal import app, db
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp
    

class ID_Form(FlaskForm):
    #Basic Contacts
    full_name = StringField('Full Name', validators=[DataRequired(), Regexp(r'^[^0-9]*$', message='Numbers are not allowed.')])
    program = StringField('Program', validators=[DataRequired(), Regexp(r'^[^0-9]*$', message='Numbers are not allowed.')])
    year_validity = StringField('Year', validators=[DataRequired(), Length(min=2, max=9)])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=8), Regexp('^[0-9-]+$')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #Signatures
    id_img = FileField('Upload ID Picture', name='id_img', validators=[FileRequired(), FileAllowed(['jpg', 'png'])], render_kw={"accept": ".png,.jpg"})
    sign_img = FileField('Upload Signature', name='sign_img', validators=[FileRequired(), FileAllowed(['jpg', 'png'])], render_kw={"accept": ".png,.jpg"})
    # Emergency Contact
    contact_person = StringField('Contact in Person', validators=[DataRequired(), Regexp(r'^[^0-9]*$', message='Numbers are not allowed.')])
    contact_number = StringField('Personal Contact Number', validators=[DataRequired(), Length(min=2, max=11),Regexp(r'^[^a-zA-Z]*$', message='Letters are not allowed.')])
    address = StringField('Address', validators=[DataRequired()])
    # Submit Field
    generate_id = SubmitField("Generate ID")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=8), Regexp('^[0-9-]+$')]) 
    remember_me = BooleanField("Remember Me")
    login = SubmitField('Login')

class DecodeForm(FlaskForm):
    img_file = FileField('Upload Photo', name='img_file', validators=[FileRequired(), FileAllowed(['jpg', 'png'])], render_kw={"accept": ".png,.jpg"})
    decode_img = SubmitField("Decode")
