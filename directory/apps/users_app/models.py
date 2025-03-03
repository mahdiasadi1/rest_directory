from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash

from directory import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(128), unique=False, nullable=False)

    @validates('password')
    def validate_password(self, key, value):
        if len(value) < 6:
            raise ValueError('Password should be atleast 6 characters.')
        return generate_password_hash(value)

    @validates('username')
    def validate_username(self, key, value):
        if not value.isidentifier():
            raise ValueError('Username is invalid.')
        return value