import os
from flask import Flask

from config import LocalDev

from security_framework import security, user_datastore, roles_required, current_user
from db.models import db, User

# Initialize the app variable to None
app = None

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

    # Return the app
    return app
    
# Call the create_app function and assign the result to the app variable
app = create_app()

# Initialize the security object with the app and the user_datastore
security.init_app(app, user_datastore)

if __name__ == '__main__':        # If this script is run directly (not imported), then run the app
    app.run()
