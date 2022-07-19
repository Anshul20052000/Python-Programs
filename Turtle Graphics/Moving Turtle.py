# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:23:49 2020

@author: hp
"""

import turtle as t
import random as rd

def inside_window():
    left_limit=(-t.window_width()/2)+100
    right_limit=(t.window_width()/2)-100
    top_limit=(t.window_height()/2)-100
    bottom_limit=(-t.window_height()/2)+100
    (x,y)=t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle():
    if inside_window():
        angle = rd.randint(0,180)
        t.right(angle)
        #t.forward(200)
        dist=rd.randint(50,300)
        t.forward(dist)
    else:
        t.backward(200)
        
t.shape('turtle')
t.fillcolor('green')
t.bgcolor('crimson')
t.speed('slow')
while True:
    move_turtle()