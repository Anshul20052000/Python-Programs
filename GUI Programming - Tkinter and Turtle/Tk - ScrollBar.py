# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:23:59 2020

@author: hp
"""

from tkinter import *
win = Tk()
scrollbar= Scrollbar(win)
scrollbar.pack(side=RIGHT,fill=Y)
List = Listbox(win,yscrollcommand=scrollbar.set)
for line in range(100):
    List.insert(END,'This is Line No.'+str(line))
List.pack(side=LEFT,fill=BOTH)
win.mainloop()