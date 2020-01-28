#  Encapsulation (Kapsülleme)
class urun:
    def __init__(self):
        self.__fiyat=1000 # Fiyat değişkeni iki tane alt tire koyarak kapsüllenir

    def fiyatyaz(self):
        print("Ürün fiyatı :",self.__fiyat)
    def setfiyat(self,fiyat): #set fiyat fonksiyonu
        self.__fiyat=fiyat
u =urun()
u.fiyatyaz()
u.__fiyat=900 # kapsüllendiği için fiyat değişmeyecektir
u.fiyatyaz()
u.setfiyat(850) # set özelliği ile kapsüllenmiş olan nesneyi değiştirdik
u.fiyatyaz()