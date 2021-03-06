# Script for Python3.* by Stephen Curtis - 12 Dec 2016


from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta

expected = ""


def calc():
    now = datetime.now()
    wdlt = e.get()
    cdlt = (int(wdlt) / 5) * 7

    due = now + timedelta(days=cdlt)

    weekday = (due.weekday())

    if weekday == 0:
        due = due + timedelta(days=4)
    elif weekday == 1:
        due = due + timedelta(days=3)
    elif weekday == 2:
        due = due + timedelta(days=2)
    elif weekday == 3:
        due = due + timedelta(days=1)
    elif weekday == 4:
        due = due + timedelta(days=0)
    elif weekday == 5:
        due = due + timedelta(days=-1)
    elif weekday == 6:
        due = due + timedelta(days=-2)
    else:
        TypeError("Possible Error: Unrecognised Week Day")

    expected = str("{}/{}/{}".format(due.day, due.month, due.year))

    result = Label(mainView, text="Expected Date: {}".format(expected), bg='#bfceff', pady=10,
                   font=('verdana', 12, 'bold'))
    result.grid(row=2, columnspan=2)


mainView = Tk()
mainView.wm_title("Lead Time Calc")
mainView.config(bg='#bfceff', padx=20, pady=15)

instruct = Label(mainView, text="Enter lead time in working days:", bg='#bfceff')
instruct.grid(row=0)
instruct.config(font=("verdana", 10, "bold"))
e = Entry(mainView, width=5)
e.grid(row=0, column=1)
calculate = Button(mainView, width=20, text="Calculate", command=calc)
calculate.grid(row=1, columnspan=2)

mainView.mainloop()