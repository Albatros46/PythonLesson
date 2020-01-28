#GUI - Scale (Slider)
import tkinter as tk
from tkinter import *

pencere=tk.Tk()
slider =Scale(from =2,to =20,orient=HORIZANTAL)
slider.place(x=10,y=10)
pencere.mainloop()