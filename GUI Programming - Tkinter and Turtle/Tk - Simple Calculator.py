# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:36:38 2020

@author: hp
"""
import tkinter
from tkinter import *
from functools import partial
win = Tk()
def Sum(label,x1,x2):
    n1=(x1.get())
    n2=(x2.get())
    Sum=int(n1)+int(n2)
    label.config(text="Sum is : %d"%Sum)
    return 
l1 = Label(win,text='First Number')
l1.grid(row=1,column=0)
l2 = Label(win,text='Second Number')
l2.grid(row=2,column=0)
label = Label(win)
label.grid(row=6,column=2)
x1 = StringVar()
x2 = StringVar()
e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=2)
Sum = partial(Sum,label,x1,x2)
button = Button(win,text='CAlCULATE',command=Sum)
button.grid(row=3,column=0)
win.mainloop()
