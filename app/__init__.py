# we used this init files to tell Python to always initialized when our lovely app start / loaded
from flask import Flask

# import config
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# load routes from app.py
from app import routes
