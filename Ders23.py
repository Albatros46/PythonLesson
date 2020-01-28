# GUI - Button ve Entry , 4 işlem uygulaması
#pencere
import tkinter as tk
def topla():#Tolama fonksiyonu
    s1=float(sayi1.get())
    s2=float(sayi2.get())
    sonuc['text']=float(s1+s2)
def cikar():#Çıkarma fonksiyonu
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc['text'] = float(s1 - s2)
def carp():#Çıkarma fonksiyonu
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc['text'] = float(s1 * s2)
def bol():#Çıkarma fonksiyonu
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc['text'] = float(s1 / s2)
pencere=tk.Tk()
pencere.title("DÖRT İŞLEM")#Pencerenin başlığı
pencere.geometry("300x300+400+200") # Pencerenin boyutu ve nerede açılacağı
sayi1=tk.Entry(width=10) # Sayi1, giriş kutusunun genişliği
sayi1.place(x=20, y=20) # Sayi1 kutusunun penceredeki konumu
sayi2=tk.Entry(width=10) # Sayi2, giriş kutusunun genişliği
sayi2.place(x=100, y=20) # Sayi2 kutusunun penceredeki konumu
sonuc=tk.Label(text="Sonuç", bg="white")#sonuc yazılacak etiketin özellikleri
sonuc['font']="Verdana 12 bold" # font, bg, ve fg burada da tanımlanabilir
sonuc['fg']="#0000FF" # HEX (16 lık) sistemle renk kodlaması da yapılır
sonuc.place(x=180,y=20)
btopla=tk.Button(text="+",font="Verdana 12 bold",command=topla).place(x=20,y=45) #Toplama font ve konumu/Command ile toplama fonksiyonu çağırıldı
bcikar=tk.Button(text="-",font="Verdana 12 bold",command=cikar).place(x=60,y=45) #Çıkarma font ve konumu/Command ile çıkarma fonksiyonu çağırıldı
bcarp=tk.Button(text="X",font="Verdana 12 bold", command=carp).place(x=100,y=45) #Çarpma font ve konumu/Command ile çarpma fonksiyonu çağırıldı
bbol=tk.Button(text="/",font="Verdana 12 bold",command=bol).place(x=140,y=45)  #Bölme font ve konumu/Command ile bol fonksiyonu çağırıldı
pencere.mainloop()