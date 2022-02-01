from app.models.db_config import *
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    # completed_at = db.Column(db.DateTime, nullable=True, default=None)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __init__(self, title, description, completed, owner_id):
        self.title = title
        self.description = description
        self.completed = completed
        self.owner_id = owner_id