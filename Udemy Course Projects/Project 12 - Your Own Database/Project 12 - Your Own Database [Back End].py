# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:27:45 2020

@author: hp
"""

import sqlite3 as s
def connect():
    conn = s.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine(ID INTEGER PRIMARY KEY, Date TEXT,Earnings INTEGER, Exercise TEXT, Study TEXT, Diet TEXT, Python TEXT)")
    conn.commit()
    conn.close()
    
def insert(date,earnings,exercise,study,diet,python):
    conn = s.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)",(date,earnings,exercise,study,diet,python))
    conn.commit()
    conn.close()
    
def view():
    conn = s.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(Id):
    conn = s.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE ID=?",(Id,))
    conn.commit()
    conn.close()
    
def search(date='',earnings='',exercise='',study='',diet='',python=''):
    conn = s.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT FROM routine WHERE Date=? OR Earnings=? OR Exercise=? OR Study=? OR Diet=? OR Python=?",(date,earnings,exercise,study,diet,python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()