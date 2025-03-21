# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy (will be linked to app later)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.Text)
    role = db.Column(db.Enum('member', 'moderator', 'admin', name='user_role'), default='member')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<User {self.email}>"