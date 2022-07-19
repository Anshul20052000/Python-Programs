# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:05:19 2020

@author: hp
"""

import turtle as t
import time as ti
def Circle():
    t.pencolor('red')
    t.circle(100)
    t.right(20)
    Circle()
t.bgcolor('black')
t.speed(100)
t.pensize(4)
Circle()
ti.sleep(2)
t.hideturtle()