# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:51:58 2020

@author: hp
"""


from tkinter import *
win = Tk()
l = Label(win,text="Username")
l.pack()
e = Entry(win)
e.pack()
t = Text(win)
t.insert(INSERT,'hello')
t.pack()
win.mainloop()