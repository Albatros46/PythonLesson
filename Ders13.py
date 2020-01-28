# Inheritance (Miras alma)
class kus: #Super sınıf
    tur_ad=""
    kus_ad=""

    def isimyaz(self):
        print("Tür Adı:",self.tur_ad)
        print("Kuş İsmi:",self.kus_ad)
class yirtici(kus): #subclass - alt sınıf
    kanat_uzunlugu="0"
    agirlik="0"
    def ozelyaz(self):
        print("Kanat Uzunluğu:",self.kanat_uzunlugu)
        print("Ağırlığı :",self.agirlik)
class kartal(yirtici): #kus ve yırtıcı sınıfın alt türü
    alt_tur=""

anadolu_kartalı=kartal()

anadolu_kartalı.tur_ad="anatolium eagle"
anadolu_kartalı.kus_ad="siyah kartal"
anadolu_kartalı.kanat_uzunlugu="1.5 m"
anadolu_kartalı.agirlik="6 kg"
anadolu_kartalı.alt_tur="middle east eagle"

anadolu_kartalı.isimyaz()
anadolu_kartalı.ozelyaz()