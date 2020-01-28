# GUI - ComboBox
import tkinter as tk # Combobox tkinter kütüphanesinde yer almıyor
from  tkinter.ttk import * # bu yüzden ttk inter kütüphanesinden bütün öğeleri çekiyoruz
def secimal():
    print(combo.get())
pencere=tk.Tk()
pencere.title("Combobox Çalışması")
pencere.geometry("300x300+200+150")
combo=Combobox() # önüne tk yazmamıza gerek yok. içeriğini burada da doldura biliriz
combo['values']=("Kahramanmaraş","İstanbul","Ankara","Adana","Antalya")
combo.current(0) # varsayılan değeri seçmek için
combo.place(x=20,y=20)
button=tk.Button(text="İşlem",command=secimal)
button.place(x=20,y=60)


pencere.mainloop()
