# FONKSİYONLAR
# def fonksiyon_adi(varsa giriş parametresi):
# """fonksiyon açıklaması yazılabilir"""
# işlemler
# reutn
def ilk_fonksiyon():
    """İLK FONKSİYON ÇALIŞMASI NASIL AMA"""
    print("İlk fonksiyon çalışması")
ilk_fonksiyon() #Fonksiyon tanımlamadan sonra çağırılır
print(ilk_fonksiyon.__doc__) #fonksiyon açıklamasını çağırmak isyorsanız

def merhaba(isim):
    print("merhaba",isim)
merhaba("Servet")

def topla(a,b):
    return a+b
print (topla(5,8))

def kuvvet(a,b):
    return a**b
print(kuvvet(2,5))