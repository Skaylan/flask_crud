from app.models.db_config import *
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    item = db.relationship('Item', backref='owner')
    
    def __init__(self, name, username, email, password_hash):
        self.name = name
        self.username = username
        self.email = email
        self.password_hash = password_hash