from flask_sqlalchemy import *
from sqlalchemy.orm import validates, relationship, backref, contains_eager, subqueryload
from sqlalchemy.ext.mutable import MutableList
from flask_security import UserMixin, RoleMixin, AsaList
from datetime import datetime


# Create an instance of the SQLAlchemy class. This object will be used as the database adapter.
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
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each venue
    name = db.Column(db.String(255), nullable=False)  # Name of the venue
    address = db.Column(db.String(), nullable=False)  # Address of the venue
    capacity = db.Column(db.Integer, nullable=False)  # Maximum capacity of the venue
    description = db.Column(db.String())  # Description of the venue

    def search(self):
        """
        This method is used to convert the Venue object into a dictionary format which can be used for JSON serialization.
        """
        return {
            'id': self.id,  # Unique identifier for the Venue
            'name': self.name,  # Name of the Venue
            'address': self.address,  # Address of the Venue
            'capacity': self.capacity,  # Capacity of the Venue
            'description': self.description  # Description of the Venue
        }
    

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each show
    name = db.Column(db.String(255))  # Name of the show
    description = db.Column(db.Text())  # Description of the show
    tags = db.Column(db.String(255))  # Tags associated with the show
    rating = db.Column(db.Float())  # Rating of the show
    ticket_price = db.Column(db.Float())  # Price of a ticket for the show
    total_tickets = db.Column(db.Integer())  # Total number of tickets available for the show
    avail_ticket = db.Column(db.Integer())  # Number of tickets currently available for the show
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))  # Foreign key referencing the venue where the show is held

    def search(self):
        """
        This method is used to convert the object into a dictionary format which can be used for JSON serialization.
        """
        return {
            'id': self.id,  # Unique identifier for the object
            'name': self.name,  # Name of the object
            'description': self.description,  # Description of the object
            'tags': self.tags,  # Tags associated with the object
            'rating': self.rating,  # Rating of the object
            'ticket_price': self.ticket_price,  # Price of the ticket for the object
            'total_tickets': self.total_tickets,  # Total number of tickets available for the object
            'avail_ticket': self.avail_ticket,  # Number of tickets currently available
            'venue_id': self.venue_id  # Identifier of the venue where the object is located
        }

class Booking(db.Model):
    __tablename__ = 'Booking'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each booking
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key referencing the user who made the booking
    show_id = db.Column(db.Integer, db.ForeignKey('Show.id'))  # Foreign key referencing the show that was booked
    booking_date = db.Column(db.DateTime())  # Date when the booking was made
    number_of_tickets = db.Column(db.Integer())  # Number of tickets booked
    total_amount = db.Column(db.Float())  # Total amount paid for the booking
    booked_tickets = db.Column(db.Integer())  # Number of tickets booked

class UserActivity(db.Model):
    __tablename__ = 'UserActivity'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user activity
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key referencing the user who performed the activity
    activity_type = db.Column(db.String(50), nullable=False)  # Type of activity performed, e.g., "login", "visit", etc.
    activity_timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the activity was performed