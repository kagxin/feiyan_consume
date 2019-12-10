from pymongo import MongoClient

mongo_uri = 'mongodb://root:root@localhost:27017'
connection = MongoClient(mongo_uri)
m = connection['demo']
