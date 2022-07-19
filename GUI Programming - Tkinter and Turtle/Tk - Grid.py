# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:39:34 2020

@author: hp
"""

from tkinter import *
win = Tk()
b=0
for i in range(10):
    for j in range(10):
        b=b+1
        Button(win,text=str(b),bd=5,borderwidth=10).grid(row=i,column=j)
        #Button(win,text=str(b),bd=5,borderwidth=10).pack()
win.mainloop()