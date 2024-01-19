# security.py
from flask_security import *
from db.models import db, User, Role
from werkzeug.security import *

admin_password = '12345678'
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
