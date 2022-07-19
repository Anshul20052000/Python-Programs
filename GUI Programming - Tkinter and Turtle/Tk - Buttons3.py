# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:10:40 2020

@author: hp
"""
from tkinter import *
win = Tk()
def ptr():
    print("Anshul Verma")
win.geometry("400x400")
b1 = Button(win,text='Button 1',command=print("hi"))
b1.place(x=0,y=0)
b2 = Button(win,text='Button 2',command=ptr,padx=20,pady=50,activeforeground='green',bg='crimson')
b2.place(y=25,x=0)
win.mainloop()
