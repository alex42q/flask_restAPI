from flask_pymongo import PyMongo

mongodb_client = PyMongo(uri='mongodb://localhost:27017/testflask')

db = mongodb_client.db