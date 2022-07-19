# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:13:34 2020

@author: hp
"""

import turtle as t
import time as ti
from itertools import cycle
colors = cycle(['red','blue','green','crimson','yellow','orange','purple','pink'])
def Circle(size,angle,forw):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(forw)
    Circle(size+5,angle+1,forw+5)
t.bgcolor('black')
t.speed(100)
t.pensize(4)
#Circle(50,40,1)
Circle(30,0,1)
ti.sleep(2)
t.hideturtle()