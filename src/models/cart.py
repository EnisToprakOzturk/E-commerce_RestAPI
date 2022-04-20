import sys
sys.path.append('../')
from config.db import db
from datetime import datetime

class CartModel(db.Model):

    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    quatity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float,nullable=False)

    createdAt = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, bullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__ (self):
        return {
            'quantity': self.quatity,
            'price': self.price,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }