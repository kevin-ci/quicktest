import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

brs_user = os.environ.get('BRS_USER')
brs_password = os.environ.get('BRS_PASSWORD')

app.config["MONGODB_NAME"] = 'book_review_site'
app.config["MONGO_URI"] = 'mongodb+srv://brs_user:brs_password@bookreviewcluster.k2d12.mongodb.net/book_review_site?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.books.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)







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















