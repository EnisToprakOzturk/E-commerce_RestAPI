from flask_sqlalchemy import SQLAlchemy
from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)

if not os.path.exist(db.sqlite):
    db.create_all()