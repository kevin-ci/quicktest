import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_review_site'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

#@app.route('/')
#@app.route('/get_books')
#def get_books():
#    return render_template("books.html", books=mongo.db.books.find())






#MONGODB_URI = os.getenv("MONGO_URI")
#DBS_NAME = "book_review_site"
#COLLECTION_NAME = "books"

#def mongo_connect(url):
#    try:
#        conn = pymongo.MongoClient(url)
#        print("Mongo is connected!")
#        return conn
#    except pymongo.errors.ConnectionFailure as e:
#        print("Could not connect to MongoDB %s") % e

#conn = mongo_connect(MONGODB_URI)

#coll = conn[DBS_NAME][COLLECTION_NAME]

#documents = coll.find()

#for doc in documents:
#    print(doc)















