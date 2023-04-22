from flask import Flask, flash, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager




app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.init_app(app)


@login.unauthorized_handler
def unauthorized():
    flash('Hakdogh ka ba? Kelangan mo muna mag login!!')
    return redirect(url_for('login'))

from pyceal import routes, models
