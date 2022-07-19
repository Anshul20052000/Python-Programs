# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:06:02 2020

@author: hp
"""

from tkinter import *
win = Tk() 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
        
def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H==0 and b%H==0:
            return H
        H-=1
        
operations = {'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,'SUB':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,'LCM':lcm,'HCF':hcf,'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,'DIVISION':div,'DIV':div,'MOD':mod,'REMAINDER':mod,'MODULUS':mod,'DIVIDE':div}

def extract_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0],l[1])
                List.delete(0,END)
                List.insert(END,r)
            except:
                List.delete(0,END)
                List.insert(END,'Something Went Wrong Please Try Again!...')
            finally:
                break
        elif word.upper() not in operations.keys():
            List.delete(0,END)
            List.insert(END,'Something Went Wrong Please Try Again!...')

win.geometry('450x300')
win.title('Smart Calculator')
win.configure(bg = 'crimson')
l1 = Label(win,text='I am a Smart Calculator',width=20,padx=3)
l1.place(x=150,y=10)
l2 = Label(win,text='My name is Calcy',padx=3)
l2.place(x=170,y=40)
l3 = Label(win,text='What can I help you?',padx=3)
l3.place(x=165,y=100)
textin = StringVar()
e1 = Entry(win,width=30,textvariable=textin)
e1.place(x=130,y=150)
b1 = Button(win,text='Just This...',command=calculate)
b1.place(x=195,y=185)
List = Listbox(win,width=40,height=3)
List.place(x=100,y=230)

win.mainloop()
