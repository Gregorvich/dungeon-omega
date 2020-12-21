import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dictFactory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
homepage = '''<h1>Dungeon Hero Archive</h1>
<p>A prototype API for interacting with the database of our Dungeon Hero project.</p>'''

@app.route("/", methods = ["GET"])
def home():
    return homepage

@app.route("api/v1/resources/sorceries/all", methods = ["GET"])
def apiAll():
    conn = sqlite3.connect("sorceries.db")
    conn.row_factory = dictFactory
    cur = conn.cursor()
    all_books = cur.execute("Select * FROM sorceries")

    return jsonify(all_books)

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route("api/v1/resources/sorceries", methods = ["GET"])
def apiFilter():
    queryParameters = request.args