# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:19:54 2020

@author: hp
"""

import turtle as t
import time as ti
from itertools import cycle
colors = cycle(['red','blue','green','crimson','yellow','orange','purple','pink'])
def Circle(size,angle,forw,shape):
    t.pencolor(next(colors))
    next_shape=''
    if shape=='circle':
        t.circle(size)
        next_shape='square'
    elif shape=='square':
        for i in range(4):
            t.forward(size*2)
            t.left(90)
        next_shape='circle'
    t.right(angle)
    t.forward(forw)
    Circle(size+5,angle+1,forw+5,next_shape)
t.bgcolor('black')
t.speed(100)
t.pensize(4)
#Circle(50,40,1)
Circle(30,0,1,'circle')
ti.sleep(2)
t.hideturtle()