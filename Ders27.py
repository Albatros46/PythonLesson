#GUI - MessageBox kullanımı
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def goster():
    messagebox.showinfo("Mesaj Metni","Hoşgeldiniz")
pencere=tk.Tk()
pencere.title("GUI - MessageBox kullanımı")
pencere.geometry("400x400+200+200")
b=Button(text="Orada Hayat Nasıl Gidiyor...",command=goster)
b.place(x=20,y=20)

pencere.mainloop()