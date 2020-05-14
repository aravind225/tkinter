# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:54:29 2020

@author: ARAVIND
"""

import calendar
from tkinter import *
root=Tk()
root.title("Calendar")
root.geometry("250x250+0+0")
e=Entry(root)
e.pack()
def month():
    global year
    year=e.get()
    e.delete(0,END)
    button_ok=Button(root,text="ok",command=ok)
    button_ok.pack()
def ok():
    global mon
    mon=e.get()
    e.delete(0,END)
    cal()
def cal():
    a=calendar.month(int(year),int(mon))
    a=a.split("\n")
    for i in a:
        my_label=Label(root,text=i)
        my_label.pack()
    

button_month=Button(root,text="month",command=month)
button_month.pack()
root.mainloop()
