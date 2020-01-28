#GUI - Scale (Slider) kaydırma çubuğu
import tkinter as tk
from tkinter import *
def degistir(val):
    etiket.configure(font="Verdana "+val)

pencere=tk.Tk()
pencere.title("GUI - Scale (Slider) kaydırma çubuğu")
pencere.geometry("1300x400+80+200")
deger=StringVar()
slider =Scale(orient=HORIZONTAL,command=degistir)
slider.place(x=10,y=10)

etiket=Label(text="SERVET AKCADAG")
etiket.place(x=20,y=80)
pencere.mainloop()