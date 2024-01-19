import os
from flask import Flask
from flask_restful import Api

from config import LocalDev

from security_framework import security, user_datastore, roles_required, current_user
from db.models import db, User



# Initialize the app variable to None
app = None
api = None

# Define the create_app function
def create_app():
    # Create an instance of the Flask class
    app = Flask(__name__, static_folder='assets')
    # Configure the app using the LocalDev class
    app.config.from_object(LocalDev)
    
    # Initialize the db object with the app
    db.init_app(app)
    # Push an application context onto the stack
    app.app_context().push()
    print('Database initialized')

    api = Api(app)
    app.app_context().push()
    print('API initialized')

    print('App setup complete.')
    # Return the app
    return app, api
    
# Call the create_app function and assign the result to the app variable
app, api_handler = create_app()

# Initialize the security object with the app and the user_datastore
security.init_app(app, user_datastore)

from routes.auth import *
api_handler.add_resource(login, '/api/login')
api_handler.add_resource(logout, '/api/logout')
api_handler.add_resource(register, '/api/register')

from routes.venue import *
api_handler.add_resource(allvenue, '/api/venue')
api_handler.add_resource(singlevenue, '/api/venue/<int:id>')

if __name__ == '__main__':        # If this script is run directly (not imported), then run the app
    app.run()
