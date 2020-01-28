# GUI - Text componenti ve çok satırlı veriler
import tkinter as tk
from tkinter import *

pencere=tk.Tk()
pencere.title("GUI - Text componenti ve çok satırlı veriler")
pencere.geometry("400x400+100+200")
t=Text(height=5,width=25,font="Arial 12",bg="gray",fg="white")
t.place(x=20,y=20)

pencere.mainloop()