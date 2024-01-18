import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDev(Config):
    # database configurations
    SQLITE_DB_DIR = os.path.join(basedir, './db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, 'db.sqlite3')
    
    # security configurations
    SECRET_KEY = "TEMPORARY_KEY_FOR_DEV" #os.environ.get('FLASK_SECRET')
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = "TEMPORARY_KEY_FOR_DEV" #os.environ.get('SECURITY_SECRET')
    SECURITY_REGISTERABLE = True
    SECURITY_JOIN_USER_ROLES = True
    SECURITY_TRACKABLE = True
    
    SECURITY_POST_LOGIN_VIEW = '/logged_in'
    SECURITY_POST_LOGOUT_VIEW = '/bye'

    SECURITY_SEND_REGISTER_EMAIL = False  # Disable automatic sending of registration confirmation email for simplicity
    SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome to My App'

    # Configure an email extension for Flask-Security
    SECURITY_EMAIL_SENDER = 'your_email@example.com'  # Replace with your email address
    SECURITY_EMAIL_REGISTERABLE = True
    # SECURITY_LOGIN_URL = '/auth/login'
    # SECURITY_LOGIN_USER_TEMPLATE = 'login_test.html'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_SECRET_KEY = "TEMPORARY_KEY_FOR_DEV" #os.environ.get('SECURITY_SECRET')
    WTF_CSRF_ENABLED = False
    JSON_SORT_KEYS = False

    # debug application
    DEBUG = True

class ProductionDev(Config):
    SQLITE_DB_DIR = os.path.join(basedir, '../db_directory')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, 'prod_db.sqlite3')
    DEBUG = False