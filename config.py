from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key'
DB_NAME = 'sanjay'

DATABASE = MongoClient()[DB_NAME]
USERS_COLLECTION = DATABASE.admin


DEBUG = True
