# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:08:36 2020

@author: hp
"""

from tkinter import *
win = Tk()
def hello():
    messagebox.showinfo("from computer",'hey there')
b = Button(win,text='Popup',command = hello)
b.pack()
win.mainloop()