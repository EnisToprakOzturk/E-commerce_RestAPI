from distutils.log import debug
from flask import Flask
from src import *
import os


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)