import math
from math import sin, cos, radians

from tkinter import *
from tkinter import ttk

#x = float(input("Введите х: "))
def calcut(c):
    if c == None: c = False
    elif c < 0.1:
        c = (c**0.5)*(c**2)
    else:
        c = math.sin(math.radians(c)) + math.cos(math.radians(c))
    return (c)

def show_message():
    label["text"] = calcut(float(entry.get()))

root = Tk()
root.title("Расчёт по формуле")
root.geometry("300x200")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Рассчитать", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()