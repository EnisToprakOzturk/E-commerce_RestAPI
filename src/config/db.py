from flask_sqlalchemy import SQLAlchemy
from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)
