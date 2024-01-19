import os
from app import create_app
from security_framework import security, user_datastore, admin_password, create_roles, admin_user_creation

from db.models import db, User, Role
from datetime import datetime


app = create_app()

with app.app_context():
    try:
        db.drop_all()
        db.create_all()
        db.session.commit()
        print('Database tables created')

        create_roles()
        print('Roles added, ie admin, user')

        admin_user_creation()
        print('Admin created')

        db.session.commit()

        


    except Exception as e:
        print(f"Error creating database tables: {e}")




    # book = book(name='book1', description='description1', section_id=1, author='author1', price=100)
    # if db.session.add(book):
    #     app.logger.info('Book added')