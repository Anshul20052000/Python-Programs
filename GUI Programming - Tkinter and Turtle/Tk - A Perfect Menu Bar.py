# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:48:28 2020

@author: hp
"""

from tkinter import *
win = Tk()
def nothing():
    file=Toplevel(win)
    button = Button(file,text='Do Nothing')
    button.pack()
menubar = Menu(win)
filemenu = Menu(menubar)
filemenu.add_command(label='New Window',command=nothing)
filemenu.add_command(label='New File',command=nothing)
filemenu.add_command(label='Open',command=nothing)
filemenu.add_command(label='Close',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Save',command=nothing)
filemenu.add_command(label='Save as',command=nothing)
filemenu.add_command(label='Clase Tab',command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Bookmarks',command=nothing)
filemenu.add_command(label='History',command=nothing)
filemenu.add_command(label='Anshul Comm.',command=nothing)
filemenu.add_command(label='Exit',command=win.quit)
menubar.add_cascade(label='File',menu=filemenu)
editmenu = Menu(menubar)
editmenu.add_command(label='Undo',command=nothing)
editmenu.add_command(label='Redo',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Cut',command=nothing)
editmenu.add_command(label='Copy',command=nothing)
editmenu.add_command(label='Paste',command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Select All',command=nothing)
editmenu.add_command(label='Exit',command=win.quit)
menubar.add_cascade(label='Edit',menu=filemenu)
win.config(menu=menubar)
win.mainloop()