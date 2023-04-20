from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__, template_folder='templates')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '65dd8a8a9be421c2b8a4f3fdcc42f36a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from pyceal import routes
