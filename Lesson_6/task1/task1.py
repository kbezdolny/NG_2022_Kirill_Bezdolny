from flask import Flask, render_template, redirect, request
import sqlite3

application = Flask("Chat")
baseName = "chatDB.db"
lastMessageId = 0

def initConnect(path):
    try:
        connection = sqlite3.connect(path)
    except sqlite3.Error as e:
        connection = None
        print(e)
    return connection

def initTables(connection):
    sqlRequest = "CREATE TABLE IF NOT EXISTS chat( id integer PRIMARY KEY, nickname text NOT NULL, message text NOT NULL);"
    connection.execute(sqlRequest)

def prepareDb(baseName):
    connection = initConnect(baseName)
    initTables(connection)
    connection.close()

prepareDb(baseName)

def setDataToBase(baseName, nickname, message):
    connection = initConnect(baseName)
    sqlRequest = "INSERT INTO chat(`nickname`, `message`) VALUES('{}', '{}')".format(nickname, message)
    cursor = connection.cursor()
    cursor.execute(sqlRequest)
    connection.commit()
    connection.close()

def getDataFromBase(baseName):
    connection = initConnect(baseName)
    sqlRequest = "SELECT * FROM chat;"
    cursor = connection.cursor()
    cursor.execute(sqlRequest)
    rows = cursor.fetchall()
    connection.close()

    resultMessage = ""
    try:
        global lastMessageId
        for row in rows:
            if lastMessageId < row[0]:
                resultMessage += f"<p><b>{row[1]}</b>: {row[2]}</p>"
                lastMessageId = row[0]
    except Exception as e:
        print(e)
    return resultMessage

@application.route("/")
def start():
    return render_template("index.html", messages=getDataFromBase(baseName))

@application.route("/chatdb")
def dbWrite():
    nickname = request.args.get("nickname")
    message = request.args.get("message")
    if nickname != None and message != None:
        setDataToBase(baseName, nickname, message)
    return getDataFromBase("chatDB.db")

application.run(host="0.0.0.0", port=8081)