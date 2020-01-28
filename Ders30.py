#GUI - Text componenti ve çok satırlı veriler
import tkinter as tk
from tkinter import *
# bir satırdan fazla yazı yazılacak ise kullanılır
pencere=tk.Tk()
pencere.title("GUI - Text componenti ve çok satırlı veriler")#Pencerenin başlığı
pencere.geometry("400x300+400+200") # Pencerenin boyutu ve nerede açılacağı
txt=Text(width=30,height=5,font="Arial 12",bg="Gray",fg="White")# text nesnesi oluşturuldu genişlik ve yükselik ayarlandı
#30 karakterlik 5 satırlık bir text nesnesi, font arkaplan renk ve yazı rengi ayarlandı.
txt.place(x=20,y=20)# text nesnesi pencereye yerleştirildi
pencere.mainloop()