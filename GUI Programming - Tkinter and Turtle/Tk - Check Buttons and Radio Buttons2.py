# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:55:46 2020

@author: hp
"""
from tkinter import *
win = Tk()
c1=IntVar()
c2=IntVar()
c3=IntVar()
cb = Radiobutton(win,text='Music',variable=c1,value=1)
cb.grid(row=0,column=1)
cb2 = Radiobutton(win,text='Value',variable=c2,value=2)
cb2.grid(row=0,column=3)
cb3 = Radiobutton(win,text='Value123',variable=c3,value=3)
cb3.grid(row=1,column=5)
win.mainloop()
