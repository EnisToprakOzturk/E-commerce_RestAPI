import sys
sys.path.append('../')
from  config.db import db
from datetime import datetime

class ImageModel(db.Model):

    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    alt = db.Column(db.String)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime())

    def __repr__(self):
        return {
            'url': self.url,
            'alt': self.alt,
            'create': self.created_at,
            'update': self.updated_at
        }