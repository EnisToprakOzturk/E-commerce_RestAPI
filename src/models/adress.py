import sys
sys.path.append('../')
from config.db import db
from datetime import datetime

class AdressModel(db.Model):

    __tablename__ = 'adress'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    province = db.Column(db.String(25), nullable=False)
    street = db.Column(db.String(25), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    phoneNumber = db.Column(db.String(10),nullable=False)
    adress = db.Column(db.String(100), nullable=False) #adresin girilmemiş kısmı için 

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__ (self):
        return {
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'province': self.province,
            'street': self.street,
            'zipcode': self.zipcode,
            'phoneNumber': self.phoneNumber,
            'adress': self.adress,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }