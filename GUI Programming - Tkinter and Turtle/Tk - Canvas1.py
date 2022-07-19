# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:40:39 2020

@author: hp
"""
from tkinter import *
win = Tk()
#win.geometry("400x400")
c = Canvas(win,height=250,width=300,bg='red')
c.grid(row=0,column=0)
c1 = Canvas(win,height=250,width=300,bg='green')
c1.grid(row=0,column=1)
c2 = Canvas(win,height=250,width=300,bg='blue')
c2.grid(row=1,column=0)
c3 = Canvas(win,height=250,width=300,bg='yellow')
c3.grid(row=1,column=1)
win.mainloop()