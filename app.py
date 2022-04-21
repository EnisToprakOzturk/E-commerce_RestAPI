from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from src import *
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)
api = Api(app)

if __name__ == "__main__":
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)