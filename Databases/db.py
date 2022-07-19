# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:27:18 2020

@author: hp
"""

import sqlite3 as sql
def createtable():
    conn = sql.connect('lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE data(Rollno INTEGER,Name TEXT,Marks REAL)')
    conn.commit()
    conn.close()
def insert(roll,nam,mark):
    conn = sql.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,nam,mark))
    conn.commit()
    conn.close()
def view():
    conn = sql.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(roll):
    conn = sql.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE Rollno=?",(roll,))
    conn.commit()
    conn.close()
def update(roll,nam,mark):
    conn = sql.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET Name=? , Marks=?  WHERE Rollno=?",(nam,mark,roll))
    conn.commit()
    conn.close()
update(23,"Anshul",20000)
print(view())
