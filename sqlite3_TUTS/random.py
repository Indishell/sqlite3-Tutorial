import json
import sqlite3
from sqlite3 import Error

import requests

with open("data_file.json", "r") as json_file:
    data = json.loads(json_file.read())

pt =  [data['chiklu']['id'] , data['chiklu']['name'], data['chiklu']['contact']]

def sql_connect():

    try:
        con = sqlite3.connect(":memory:")
        return con

    except:
        print(Error)


def sql_table(con):
    
    cursorObj = con.cursor()
    cursorObj.execute('CREATE TABLE SCHOOL(id INTEGER PRIMARY KEY, name text, contact integer)')
    con.commit()


def sql_insert(con, pt):

    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO SCHOOL VALUES (? , ? , ?) ", pt)
    con.commit()


def sql_fetch(con):

    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM SCHOOL')

    for i in cursorObj.fetchall():
        with open("pkk.json", "w") as js2:
            json.dump(i, js2, indent=4)


con =  sql_connect()
sql_table(con)

sql_insert(con, pt)

sql_fetch(con)