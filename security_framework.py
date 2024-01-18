# security.py
from flask_security import *
from db.models import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
