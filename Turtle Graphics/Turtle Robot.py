# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:38:56 2020

@author: hp
"""

import turtle as t
def rec(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow')
t.bgcolor('Dodger Blue')
t.goto(-100,-150)
rec(50,20,'blue')
t.goto(-30,-150)
rec(50,20,'blue')
t.goto(-25,-50)
rec(15,100,'grey')
t.goto(-70,-50)
rec(15,100,'grey')
t.goto(-90,100)
rec(100,150,'red')
t.goto(-150,70)
rec(60,15,'grey')
t.goto(-150,110)
rec(15,40,'grey')
t.goto(10,70)
rec(60,15,'grey')
t.goto(55,110)
rec(15,40,'grey')
t.goto(-50,120)
rec(15,20,'grey')
t.goto(-85,170)
rec(80,50,'red')
t.goto(-60,160)
rec(30,10,'white')
t.goto(-55,155)
rec(5,5,'black')
t.goto(-40,155)
rec(5,5,'black')
t.goto(-65,138)
rec(40,5,'black')
t.hideturtle()
