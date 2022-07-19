# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:28:48 2020

@author: hp
"""

import psycopg2 as p
def createtable():
    conn = p.connect("dbname='Data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE data(Rollno INTEGER,Name TEXT,Marks REAL)')
    conn.commit()
    conn.close()
def insert(roll,nam,mark):
    conn = p.connect("dbname='Data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll,nam,mark))
    conn.commit()
    conn.close()
def view():
    conn = p.connect("dbname='Data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(roll):
    conn = p.connect("dbname='Data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE Rollno=%s",(roll,))
    conn.commit()
    conn.close()
def update(roll,nam,mark):
    conn = p.connect("dbname='Data2' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE data SET Name=%s , Marks=%s WHERE Rollno=%s", (nam,mark,roll))
    conn.commit()
    conn.close()
print(view())
update(23,"Anshul",200000)
print(view())