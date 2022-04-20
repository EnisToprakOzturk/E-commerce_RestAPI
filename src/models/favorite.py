import sys
sys.path.append('../')
from config.db import db
from datetime import datetime

class FavoriteModel(db.Model):

    __tablename__ = 'favorite'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__ (self):
        return {
            'id': self.id,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }