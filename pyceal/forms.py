from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
    

class ID_Form(FlaskForm):
## Req Contacts 
    full_name = StringField('Full Name', validators=[DataRequired()])
    program = StringField('Program', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=10)])
    year = StringField('Year', validators=[DataRequired(), Length(min=2, max=4)])
    ## ADD EMAIL 

## EMERGENCY CONTACT
    contact_person = StringField('Contact_person', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    contact_number = StringField('Contact_number', validators=[DataRequired()])
## Submit Field
    generate_id = SubmitField("Generate ID")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    sr_code = StringField('Sr_code', validators=[DataRequired(), Length(min=2, max=10)]) 
    remember = BooleanField("Remember Me")
    login = SubmitField('Login')

