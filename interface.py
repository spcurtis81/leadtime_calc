#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 12 Dec 2016


from leadtime_calc import *
from tkinter import *

mainView = Tk()
mainView.wm_title("Lead Time Calc")
mainView.geometry("{}x{}".format(300, 300))

Label(mainView, text="Enter lead time in working days:").pack()

v = StringVar()
e = Entry(mainView, textvariable=v)
e.pack()

v.set("a default value")
s = v.get()

Button(mainView, text="Calculate").pack()
Label(mainView, text="Expected Date: {}".format(expected)).pack()




mainView.mainloop()