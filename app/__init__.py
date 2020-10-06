# we used this init files to tell Python to always initialized when our lovely app start / loaded

from flask import Flask

app = Flask(__name__)

# load routes from app.py
from app import routes
