# GUI - Spinbox
import tkinter as tk
from tkinter import *
# RGB= RED GREEN BLUE (
def renk():
    r=sred.get() # Kırmızıyı tanımladık
    g=sgreen.get() #Yeşili tanımladık
    b=sblue.get() #Maviyi tanımladık
    # HEXDEIMAL 16'lık koda çevirmemiz lazım renkleri
    rh=hex(int(r)) # red önce intiger a sonra hexedecimal e çevirildi
    rg = hex(int(g)) # green önce intiger a sonra hexedecimal e çevirildi
    rb = hex(int(b)) # blue önce intiger a sonra hexedecimal e çevirildi
    color="#"+rh.replace("0x","")+rg.replace("0x","")+rb.replace("0x","")
    # HEXDECIMEL sayılarda sayının önünde bulunan #0x kaldırdık çünkü program çalışsa da kod işe yaramaz
    print(color)
    pencere.configure(bg=color)
pencere=tk.Tk()
pencere.title("Spinbox Dersi")
pencere.geometry("400x400+200+200")

lred=Label(text="Kırmızı")# Kırmızı etiket
lred.place(x=30,y=50)# Kırmızı etiket konumu
sred=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)# Kırmızı Spinbox
sred.place(x=80,y=50)

lblue=Label(text="Mavi")
lblue.place(x=40,y=80)
sblue=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk) # Sarı Spinbox
sblue.place(x=80,y=80)

lgreen=Label(text="Yeşil")
lgreen.place(x=40,y=110)
sgreen=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk) # Yeşil  Spinbox
sgreen.place(x=80,y=110)

pencere.mainloop()