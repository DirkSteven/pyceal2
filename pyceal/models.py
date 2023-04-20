from datetime import datetime
from pyceal import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # sr_code = db.Column (db.String(60), unique=True, nullable=False)
    # date_added = db.Column(db.String(20), db.DateTime, default=datetime.utcnow, nullable=False)


    def __repr__(self):
        return f"User ('{self.username}')"