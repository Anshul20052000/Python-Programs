# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:51:28 2020

@author: hp
"""

from tkinter import *
win = Tk()
frame = Frame(win)
frame.pack()
frame2 = Frame(win)
frame2.pack()
rb = Button(frame,text='Red',fg='red',bg='black')
rb.pack(side=LEFT)
gb = Button(frame,text='Green',fg='green')
gb.pack(side=LEFT)
bb = Button(frame,text='Blue',fg='blue')
bb.pack(side=LEFT)
blb = Button(frame,text='Black',fg='black')
blb.pack(side=LEFT)
yb = Button(frame,text='Yellow',fg='yellow')
yb.pack(side=LEFT)
win.mainloop()
