# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:55:46 2020

@author: hp
"""
from tkinter import *
win = Tk()
c1=IntVar()
c2=IntVar()
cb = Checkbutton(win,text='Music',offvalue=0,onvalue=1,height=5,width=10,variable=c1)
cb.grid(row=0,column=1)
cb2 = Checkbutton(win,text='Value',offvalue=0,onvalue=1,height=50,width=100,variable=c2)
cb2.grid(row=0,column=3)
print(c1,c1)
win.mainloop()
