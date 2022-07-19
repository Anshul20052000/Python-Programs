# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:44:29 2020

@author: hp
"""

from tkinter import *
win = Tk()
def total():
    a = e1.get()
    b = e2.get()
    print(int(a)+int(b))
l1 = Label(win,text='Maths')
l1.place(x=10,y=10)
e1 = Entry(win,bd=5)
e1.place(x=60,y=10)
l2 = Label(win,text='English')
l2.place(x=10,y=60)
e2 = Entry(win,bd=5)
e2.place(x=60,y=60)
b = Button(win,text='Submit',command=total)
b.place(x=100,y=100)
win.mainloop()