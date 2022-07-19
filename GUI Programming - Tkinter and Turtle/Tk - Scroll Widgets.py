# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:22:49 2020

@author: hp
"""

from tkinter import *
win = Tk()
s = Scale(win)
s.pack()
sb = Spinbox(win,from_ = 0 ,to=10)
sb.pack()
win.mainloop()
