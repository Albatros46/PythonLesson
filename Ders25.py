# GUI - CheckButton ve RadioButton
import tkinter as tk
from tkinter import * # tkinter kütüphanesinin tümü çağırıldı
def sec():
    print("Seçim 1",c1.get())
    print("Seçim 2",c2.get())
def radio():
    print("Bay",r.get())
    print("Bayan", r.get())
pencere=tk.Tk()
pencere.title("Checkbutton ve Radiobutton dersi")#pencere başlığı
pencere.geometry("400x300+200+200")#Pencere boyutu ve ekranda açılacağı koordinat
c1=IntVar()
c2=IntVar()
cbutton1=Checkbutton(text="Secim 1",variable=c1,onvalue=1,offvalue=0,command=sec)
# variable sayısal değer ataması için yukarıda tanımlandı
# ovalue seçim yapılmış ise 1 , offvalue seçim yapılmadıysa 0 değerini al
cbutton1.place(x=20,y=20)#ekrandaki konumu
cbutton2=Checkbutton(text="Secim 2",variable=c2,onvalue=1,offvalue=0,command=sec)
cbutton2.place(x=20,y=40)#ekrandaki konumu
#------------RadioButton-----------------------
#radibuttonlar için bir tane değişken tanımlanır
r=IntVar()
rbutton1=Radiobutton(text="Bay",variable=r,value=1,command=radio)
rbutton2=Radiobutton(text="Bayan",variable=r,value=2,command=radio)
rbutton1.place(x=100,y=20)
rbutton2.place(x=100,y=40)
pencere.mainloop()