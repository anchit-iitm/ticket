from flask_sqlalchemy import *
from sqlalchemy.orm import validates, relationship, backref, contains_eager, subqueryload
from sqlalchemy.ext.mutable import MutableList
from flask_security import UserMixin, RoleMixin, AsaList
from datetime import datetime

db = SQLAlchemy()

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(MutableList.as_mutable(AsaList()), nullable=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    
    def __init__(self, email, password, active=True, roles=None, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.active = active

        # Fetch the 'student' role from the database
        student_role = Role.query.filter_by(name='student').first()

        # Assign the role to the user if it exists
        if student_role:
            self.roles = [student_role]
        else:
            self.roles = []




class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String())
    

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text())
    tags = db.Column(db.String(255))
    rating = db.Column(db.Float())
    ticket_price = db.Column(db.Float())
    total_tickets = db.Column(db.Integer())
    avail_ticket = db.Column(db.Integer())
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    booking_date = db.Column(db.DateTime())
    number_of_tickets = db.Column(db.Integer())
    total_amount = db.Column(db.Float())
    booked_tickets = db.Column(db.Integer())

class UserActivity(db.Model):
    __tablename__ = 'UserActivity'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)  # e.g., "login", "visit", etc.
    activity_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
