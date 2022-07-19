# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:46:24 2020

@author: hp
"""
from tkinter import *
win = Tk()
c = Canvas(win,height=250,width=300,bg='green')
coord=10,50,240,210
arc = c.create_arc(coord,start=0,extent=150,fill='red')
c.pack()
win.mainloop()