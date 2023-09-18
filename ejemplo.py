# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:15:54 2021

@author: Derly garzon
"""

from tkinter import *
from tkcalendar import Calendar,DateEntry


root = Tk()

cal = DateEntry(root,width=30,bg="darkblue",fg="white",year=2023)

cal.grid()

root.mainloop()