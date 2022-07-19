# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:10:40 2020

@author: hp
"""
from tkinter import *
win = Tk()
win.geometry("400x400")
b1 = Button(win, text='Button 1')
b1.grid(row=1,column=0)
b2 = Button(win, text='Button 2')
b2.grid(row=1,column=1)
win.mainloop()
