import sqlite3


def initConnect(path: str) -> object:
    try:
        connection = sqlite3.connect(path)
    except sqlite3.Error as e:
        connection = None
        print(e)
    return connection


def initTables(connection: object):
    sqlRequest = "CREATE TABLE IF NOT EXISTS data( id integer PRIMARY KEY, name text NOT NULL, value text NOT NULL);"
    connection.execute(sqlRequest)


def prepareDB(baseName: str):
    connection = initConnect(baseName)
    initTables(connection)
    connection.close()


def clearDataInDB(baseName: str):
    connection = initConnect(baseName)
    cursor = connection.cursor()
    sqlRequest = "DELETE from data where 1"
    cursor.execute(sqlRequest)
    connection.commit()
    connection.close()


def setDataToDB(baseName: str, name: str, value: str or int or float):
    connection = initConnect(baseName)
    cursor = connection.cursor()
    sqlRequest = "INSERT INTO data(`name`, `value`) VALUES('{}', '{}')".format(name, value)
    cursor.execute(sqlRequest)
    connection.commit()
    connection.close()


def getDataFromDB(baseName: str) -> list:
    connection = initConnect(baseName)
    cursor = connection.cursor()
    sqlRequest = "SELECT * FROM data;"
    cursor.execute(sqlRequest)
    rows = cursor.fetchall()
    connection.close()

    pcDataList = []
    for row in rows:
        dataName = row[1].replace("_", " ").title() + ": "
        pcDataList.append({dataName:row[2]})
    return pcDataList
