from datetime import datetime
from pyceal import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), unique=True, nullable=False)
#     program = db.Column(db.String(20), unique=True, nullable=True)
#     year = db.Column(db.String(20), unique=True, nullable=True)
#     sr_code = db.Column (db.String(60), unique=True, nullable=True)
    
#     full_name = db.Column(db.String(20), unique=True, nullable=True)
#     email = db.Column(db.String(120), unique=True, nullable=True)
#     image_file = db.Column(db.String(20), nullable=True, default='default.jpg')


# ## Contacts

#     contact_person = db.Column(db.String(20), unique=True, nullable=True)
#     address = db.Column(db.String(20), unique=True, nullable=True)
#     contact_number = db.Column(db.String(20), unique=True, nullable=True)


    # date_added = db.Column(db.String(20), db.DateTime, nullable=False, default=datetime.utcnow,)


    def __repr__(self):
        return f"User ('{self.full_name}')"