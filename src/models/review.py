import sys
sys.path.append('../')
from config.db import db
from datetime import datetime

class ReviewModel(db.Model):

    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    rate = db.Column(db.Float)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__ (self):
        return {
            'id': self.id,
            'comment': self.comment,
            'rate': self.rate,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }