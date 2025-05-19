from datetime import datetime
from pyceal import db, login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), unique=True, nullable=False)
    program = db.Column(db.String(20), nullable=True)
    year_validity = db.Column(db.String(20), nullable=True)
    sr_code = db.Column (db.String(8), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    ### IMAGE
    id_img_data = db.Column(db.LargeBinary, nullable=False)
    id_img_name = db.Column(db.Text, nullable=False)
    id_img_mimetype = db.Column(db.Text, nullable=False)
    ### E-SIG
    sign_img_data = db.Column(db.LargeBinary, nullable=False)
    sign_img_name = db.Column(db.Text, nullable=False)
    sign_img_mimetype = db.Column(db.Text, nullable=False)
    ## Contacts
    contact_person = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(20), nullable=True)
    contact_number = db.Column(db.String(20), nullable=True)

    def __repr__(self):

        return f"User ('{self.full_name}')"
    

    def check_srcode(self, sr_code):
        if self.sr_code == sr_code:

            return True
        
        return False


@login.user_loader
def load_user(id):
    
    return User.query.get(int(id))