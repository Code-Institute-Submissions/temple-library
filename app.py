import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo  # To get Flask interacting with MongoDB #
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'temple_library'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/book')
def book():
    return render_template("book.html", book=mongo.db.book.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
