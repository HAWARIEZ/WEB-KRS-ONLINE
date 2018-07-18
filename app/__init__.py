from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager=LoginManager(app)
login_manager.login_view ='login_mhs'
login_manager.login_message = 'Login dulu pak!'

from app.models import models
from app.routes import routes





