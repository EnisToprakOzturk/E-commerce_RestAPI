import sys
sys.path.append('../')
from config.db import db
from datetime import datetime

class ProductModel(db.Model):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    brand = db.Column(db.String)
    barcode = db.Column(db.String)
    quantity = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    createdAt = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, bullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__ (self):
        return {
            'name': self.name,
            'description': self.description,
            'brand': self.brand,
            'barcode': self.barcode,
            'quantity': self.quantity,
            'price': self.price,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
