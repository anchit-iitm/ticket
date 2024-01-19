import os
from app import create_app
from security_framework import security, user_datastore, create_roles, admin_user_creation

from db.models import *
from datetime import datetime


# Create an instance of the application
app, api = create_app()

# Use the application context to ensure that the database operations are performed in the right context
with app.app_context():
    try:
        # Drop all existing tables in the database
        db.drop_all()
        # Create all tables defined in the SQLAlchemy models
        db.create_all()
        # Commit the changes to the database
        db.session.commit()
        # Print a message to indicate that the tables have been created
        print('Database tables created')

        # Call the function to create roles
        create_roles()
        # Print a message to indicate that the roles have been added
        print('Roles added, ie admin, user')

        # Call the function to create the admin user
        if admin_user_creation():
            # Print a message to indicate that the admin user has been created
            print('Admin created')

        # create 2 venues
        venue1 = Venue(
            name='venue1', 
            address='address1', 
            capacity=100, 
            description='description1'
            )
        db.session.add(venue1)
        venue2 = Venue(
            name='venue2', 
            address='address2', 
            capacity=200, 
            description='description2'
            )
        db.session.add(venue2)

        db.session.commit()

        # create 2 shows
        show1 = Show(
            name='show1', 
            description='description1', 
            tags='tag1, tag2', 
            rating=4.5, 
            ticket_price=100.0, 
            total_tickets=200, 
            avail_ticket=200, 
            venue_id=1
        )
        db.session.add(show1)

        show2 = Show(
            name='show2', 
            description='description2', 
            tags='tag3, tag4', 
            rating=4.0, 
            ticket_price=150.0, 
            total_tickets=300, 
            avail_ticket=300, 
            venue_id=2
        )
        db.session.add(show2)

        # Commit any changes to the database
        db.session.commit()
        


    except Exception as e:
        print(f"Error creating database tables: {e}")




    # book = book(name='book1', description='description1', section_id=1, author='author1', price=100)
    # if db.session.add(book):
    #     app.logger.info('Book added')