import os
from app import create_app
from security_framework import security, user_datastore, admin_password, generate_password_hash, verify_password

from db.models import db, User, Role
from datetime import datetime


app = create_app()

with app.app_context():
    try:
        db.drop_all()
        db.create_all()
        db.session.commit()
        print('Database tables created')

        admin = Role(name='admin', description='app_admin')
        db.session.add(admin)

        user = Role(name='user', description='gen_user')
        db.session.add(user)

        print('Roles added, ie admin, librarian, student')
        db.session.commit()

        hashed_password = generate_password_hash(admin_password)
        usr_librarian = user_datastore.create_user(email='abc@abc.com', password=hashed_password)
        user_datastore.add_role_to_user(usr_librarian, 'admin')
        if usr_librarian:
            print('Librarian added')

        db.session.commit()

        test_password = '12345678'


    except Exception as e:
        print(f"Error creating database tables: {e}")




    # book = book(name='book1', description='description1', section_id=1, author='author1', price=100)
    # if db.session.add(book):
    #     app.logger.info('Book added')