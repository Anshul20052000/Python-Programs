# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:02:47 2020

@author: hp
"""

from tkinter import *
win = Tk()
lb = Listbox(win)
lb.insert(1,'Python')
lb.insert(2,'C/C++')
lb.insert(3,'Java')
lb.insert(4,'Query')
lb.insert(5,'SQL')
lb.insert(6,'Ruby')
lb.pack()
win.mainloop()