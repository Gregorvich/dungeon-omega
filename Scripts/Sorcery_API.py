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

@app.route("/api/v1/resources/sorceries/all", methods = ["GET"])
def apiAll():
    database = sqlite3.connect("Database_Objects/sorceries.db")
    database.row_factory = dictFactory
    cur = database.cursor()
    all_books = cur.execute("SELECT * FROM Sorceries").fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route("/api/v1/resources/sorceries", methods = ["GET"])
def apiFilter():
    queryParameters = request.args
    
    name = queryParameters.get("name")
    MPCost = queryParameters.get("mp_cost", -1, type = int)
    element = queryParameters.get("elemental_alignment")
    forbiddenStatus = queryParameters.get("forbidden_status", -1, type = int)
    forbiddenStatus = bool(forbiddenStatus)

    query = "SELECT * FROM Sorceries WHERE"
    sorceryInfo = {}

    if name:
        query += " name = :sorceryName AND"
        sorceryInfo["sorceryName"] = name
    if (MPCost != -1):
        query += " MPCost = :sorceryManaCost AND"
        sorceryInfo["sorceryManaCost"] = MPCost
    if element:
        query += " element = :sorceryElement AND"
        sorceryInfo["sorceryElement"] = element
    if (forbiddenStatus != -1):
        query += " forbiddenStatus = :sorceryForbiddenStatus AND"
        sorceryInfo["sorceryForbiddenStatus"] = forbiddenStatus
    if not (name or (MPCost != -1) or element or (forbiddenStatus != -1)):
        return pageNotFound(404)

    query = query[:-4] + ";"

    database = sqlite3.connect("Database_Objects/sorceries.db")
    database.row_factory = dictFactory
    cur = database.cursor()

    results = cur.execute(query, sorceryInfo).fetchall()
    
    return jsonify(results)

app.run()