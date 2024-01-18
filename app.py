import os

from flask import Flask

from config import LocalDev
from security_framework import security, user_datastore, roles_required, current_user
from db.models import db, User


# set app = None to initialize variable
app = None

def create_app():
    app = Flask(__name__, static_folder='assets')
    app.config.from_object(LocalDev)
    
    db.init_app(app)
    app.app_context().push()

    return app
    
app = create_app()
security.init_app(app, user_datastore)


# @roles_required('admin')
# @app.route('/init_app')
# def init_app():
#     add_section = User(email='test1', password='test1', roles=['admin'], username='test1', fs_uniquifier='test1')
#     db.session.add(add_section)
#     db.session.commit()
#     return "App initialized"


if __name__ == '__main__':
    app.run()
