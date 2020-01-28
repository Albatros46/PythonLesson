# GUI-Pencere Oluşturma Kullanıcı arayüzü
# Python ile Gösel Programla işlemi
import tkinter as tk
pencere=tk.Tk()
# Tasarım ve çalışacak kodlar bu noktaya yazılacak
pencere.title("Arayüz Programı") # pencere başlığı
pencere.geometry("500x300+450+120") # Pencere genişliği 500x300
                    # Pencerenin ekranda açılacağı yer 450+120
etiket=tk.Label(text="Ad Soyad :",font="Verdana 22 bold")
etiket.pack() # Etiketi pencereye yerleştirdik
#pack() komponentleri paketler
#grid() arayüzün parçalara bölündüğünü kabul ederek çalışır
#palace() yönteminde ise X ve Y koordinatları ile nesne yerleştirilir
pencere.mainloop()