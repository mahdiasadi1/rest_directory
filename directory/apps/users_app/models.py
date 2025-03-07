from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from directory import db, bcrypt  # Import bcrypt from your app

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(128), unique=False, nullable=False)

    @validates('password')
    def validate_password(self, key, value):
        if value is None:
            raise ValueError('Password can\'t be null')
        if len(value) < 6:
            raise ValueError('Password should be atleast 6 characters.')
        return bcrypt.generate_password_hash(value).decode('utf-8')  # Hash and decode

    @validates('username')
    def validate_username(self, key, value):
        if value is None:
            raise ValueError('Username can\'t be null')
        if not value.isidentifier():
            raise ValueError('Username is invalid.')
        return value

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)