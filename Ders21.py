# GUI - Çoklu Pencereler ile çalışmak , mainloop
# çoklu pencerelerle çalışmak
import tkinter as tk
pencere1=tk.Tk() # ekrana pencere basılırken ekran hertz kadar pencere basar
pencere1.title("BİRİNCİ PENCEREM") #pencerenin başlığı
pencere1.geometry("500x300+450+120")# pencerenin boyutu ve nerede açılacağı
pencere1.configure(bg="red")#penerenin arkaplan rengi
pencere1.mainloop()

pencere2=tk.Tk() # BİRİNCİ PENCERE KAPANINCA İKİNCİ PENCERE AÇILACAKTIR
pencere2.title("İKİNCİ PENCEREM")
pencere2.configure(bg="yellow") #penerenin arkaplan rengi
pencere2.mainloop()

pencere3=tk.Tk() # BİRİNCİ PENCERE KAPANINCA İKİNCİ PENCERE AÇILACAKTIR
pencere3.title("ÜÇÜNCÜ PENCEREM")
pencere3.configure(bg="blue")#penerenin arkaplan rengi
pencere3.mainloop()