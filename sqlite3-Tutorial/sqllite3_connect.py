import sqlite3
from sqlite3 import Error

def sql_connection():

    try:
        con = sqlite3.connect('newdb.db')
        return con

    except Error:
        print(Error)


def sql_table(con):

    cursorObj = con.cursor()
    cursorObj.execute('CREATE TABLE EMPLOYEE(id integer PRIMARY KEY, name text, salary real, department text, designation text, hireDate text) VALUES(?, ?, ?, ?, ? , ?)', entities)
    con.commit()


def sql_insert(con, entities):
    cursorObj = con.cursor()
    
    cursorObj.executemany('INSERT INTO EMPLOYEE(id, name, salary, department, designation, hireDate) VALUES(?, ?, ?, ?, ? , ?)', entities)
    con.commit()


def sql_fetch(con):

    cusrorObj = con.cursor()
    cusrorObj.execute('SELECT id, name, hireDate, from EMPLOYEE WHERE salary > 80000')

    rows = cusrorObj.fetchall()
    for row in rows:
        print(row)
        
        
def sql_update(con):
    cusrorObj = con.cursor()
    cusrorObj.execute('UPDATE EMPLOYEE SET name = "Sir Anurag" WHERE id = 1616')
    con.commit()



con = sql_connection()
sql_table(con)
entities = [ (1616, 'Anurag Mishra', 185000, 'Tech', 'Engineering Manager', '2020-05-06')  , (1617, 'Rajesh Mishra', 235000, 'EXCV', 'Senior Manager', '1988-05-06')]
sql_insert(con, entities)

sql_update(con)
sql_fetch(con)
