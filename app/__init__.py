"""Maybe the root of flask app?"""
import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


load_dotenv(find_dotenv())  # default ==> filename = ".env"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db, directory="app/migrations")

from app.models import MovieModel
from app.routes import MovieRoute
