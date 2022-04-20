import sys
sys.path.append('../')
from  config.db import db

class CategoryModel(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=db.func.now())

    def get_summary(self): 
        return {
            'id': self.id,
            'name': self.name,
            'time': self.createdAt
        }
    
    def __repr__(self):
        return self.name