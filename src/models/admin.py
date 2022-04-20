import sys 
sys.path.append('../')
from  config.db import db


class AdminModel(db.Model):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    updatedAt = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f"Admin(name = {'name'}, password = {'password'}, email = {'email'}, createdAt = {'createdAt'}, updatedAt = {'updatedAt'})"
