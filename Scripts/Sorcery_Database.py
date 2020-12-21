import sqlite3
from Sorcery_Functions import Sorcery
from Sorcery_Functions import createSpells

database = sqlite3.connect("Database_Objects/sorceries.db")
cur = database.cursor()

cur.execute("""CREATE TABLE Sorceries (
    name TEXT,
    MPCost INTEGER,
    element TEXT,
    forbiddenStatus INTEGER)""")

spellList = createSpells(True, True)

def insertSorcery(sorcery):
    query = "INSERT INTO Sorceries VALUES(:name, :MPCost, :element, :forbiddenStatus)"
    sorceryInfo = {"name": sorcery.getName(), "MPCost": sorcery.getMPCost(),
                "element": sorcery.getElementalAlignment(), "forbiddenStatus": sorcery.getForbiddenStatus()}
    cur.execute(query, sorceryInfo)
    database.commit()

def deleteSorcery(sorcery):
    query = "DELETE FROM Sorceries WHERE name = :name"
    sorceryInfo = {"name": sorcery.getName()}
    cur.execute(query, sorceryInfo)
    database.commit()

def getAllSorceries():
    query = "SELECT * FROM Sorceries"
    cur.execute(query)
    return cur.fetchall()

def getSorceryByName(sorcery):
    query = "SELECT * FROM Sorceries WHERE name = :name"
    sorceryInfo = {"name": sorcery.getName()}
    cur.execute(query, sorceryInfo)
    return cur.fetchone()

def getSorceryByElement(sorcery):
    query = "SELECT * FROM Sorceries WHERE element = :element"
    sorceryInfo = {"element": sorcery.getElementalAlignment}
    cur.execute(query, sorceryInfo)
    return cur.fetchall()

def updateMPCost(sorcery, newMPCost):
    query = """UPDATE Sorceries SET MPCost = :MPCost WHERE
            name = :name"""
    sorceryInfo = {"name": sorcery.getName(), "MPCost": newMPCost}
    cur.execute(query, sorceryInfo)
    database.commit()

for sorcery in spellList:
    insertSorcery(sorcery)

print(getAllSorceries())
database.close()