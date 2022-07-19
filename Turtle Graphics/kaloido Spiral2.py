# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:11:43 2020

@author: hp
"""

import turtle as t
import time as ti
def Circle(color,size,angle):
    t.pencolor(color)
    t.circle(size)
    t.right(angle)
    Circle(color,size,angle)
t.bgcolor('black')
t.speed(100)
t.pensize(4)
Circle('red',100,40)
ti.sleep(2)
t.hideturtle()