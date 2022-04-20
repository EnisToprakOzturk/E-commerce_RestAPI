from datetime import datetime
from config.db import db
import sys
sys.path.append('../')


class UserModel(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    dateOfBirth = db.Column(db.Datetime, nullable=False)

    adresses = db.relationship('adress', backref='user')

    createdAt = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.Datetime, nullable=False,
                          default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'dateOfBirth': self.dateOfBirth,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
