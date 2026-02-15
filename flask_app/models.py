"""
Handles Structure of the data
"""

from flask_app.database import db

class User(db.Model):
    __tablename__ = 'usr'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pswd = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'