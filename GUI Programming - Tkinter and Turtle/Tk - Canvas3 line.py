# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:46:24 2020

@author: hp
"""
from tkinter import *
win = Tk()
c = Canvas(win,height=2500,width=3000,bg='white')
arc = c.create_line(10,10,200,200,fill='red')
arc1 = c.create_line(200,200,600,500,fill='blue')
arc2 = c.create_line(600,500,0,0,fill='green')
arc3 = c.create_line(0,0,1200,2100,fill='orange')
arc4 = c.create_line(1200,2100,30,210,fill='yellow')
arc5 = c.create_line(30,210,10,100,fill='crimson')
c.pack()
win.mainloop()