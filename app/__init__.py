from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from .config import Config

# import flask migrate here
from flask_migrate import Migrate


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views