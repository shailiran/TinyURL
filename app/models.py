from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db, login_manager

# class Employee(UserMixin, db.Model):
#     """
#     Create an Employee table
#     """

#     # Ensures table will be named in plural and not in singular
#     # as is the name of the model
#     __tablename__ = 'employees'

#     id = db.Column(db.Integer, primary_key=True)


# class Department(db.Model):
#     """
#     Create a Department table
#     """

#     __tablename__ = 'departments'

#     id = db.Column(db.Integer, primary_key=True)

class URL(db.Model):
    """
    Create URL table
    """

    ___tablename___ = 'urls'

    id = db.Column('id_', db.Integer, primary_key=True)
    original_url = db.Column('original_url', db.String())
    short_url = db.Column('short_url', db.String(8), unique=True)

    def __init__(self, original, short):
        self.original_url = original
        self.short_url = short
