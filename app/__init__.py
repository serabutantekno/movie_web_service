"""Maybe the root of flask app?"""
from dotenv import find_dotenv, load_dotenv
from flask import Flask

load_dotenv(find_dotenv())  # default ==> filename = ".env"
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Just an initial function from official documentation."""
    return 'Hello, World!'
