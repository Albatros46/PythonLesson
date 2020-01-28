# GUI Layout-Pack, Grid,Place
import tkinter as tk
pencere=tk.Tk()
pencere.geometry("300x300")
pencere.title("PYTHON İLE GÖRSEL PROG.")# bg-arkaplan fg-yazı rengi font-yazı fontu
etiket1=tk.Label(text="Ad Soyad :",font="Verdana", bg="blue",fg="yellow")
etiket1.pack(side="left") # Sola Hizaladık, side ile hizalayabiliyoruz
etiket2=tk.Label(text="Doğum Tarihi :",font="Verdana", bg="red",fg="white")
etiket2.pack(side="right")# left, right, top ve bottom şeklinde kullanılır
etiket3=tk.Label(text="Doğum Yeri :",font="Verdana", bg="green",fg="white")
etiket3.pack(fill="x") # X ve Y eksenlerinde kalan yeri tutar
etiket4=tk.Label(text="Medeni Hali :",font="Verdana", bg="red",fg="white")
etiket4.pack(expand="yes") #Yes ve No ekranda kalan yere konumlanır
pencere.mainloop()

pencere1=tk.Tk()
pencere1.geometry("300x300")
p2e1=tk.Label(text="SERVET",font="Verdana", bg="red",fg="white")
p2e1.grid(row=1,column=1) # grid ile konuma belirliyoruz 0 a 0 konumunda yerleşecek
p2e2=tk.Label(text="SERVET",font="Verdana", bg="red",fg="white")
p2e2.grid(row=2,column=1) # grid ile konuma belirliyoruz 0 a 0 konumunda yerleşecek
pencere1.mainloop()

pencere2=tk.Tk()
p3e1=tk.Label(text="SERVET",font="Verdana", bg="red",fg="white")
p3e1.place(x=20,y=25) # Place ile X ve Y koordinatları ile isteğiniz yere yerleştirebilirsiniz
pencere2.mainloop()
