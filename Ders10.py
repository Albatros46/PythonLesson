# Class and Object (SInıflar ve Nesneler)
class ogrenci: #ogrenci adında sınıf oluşturuldu
    ad="Servet" #sınıfın içine değişlenler tanımlandı
    soyad="Akçadağ"
    def yazdir(self): #sınıf içine yazdır fonksiyonu tanımlandı
        print(self.ad)
        print(self.soyad)
    def ortalama(self,vize,final):
        return vize*0.4+final*0.66
nesne=ogrenci() #nesne oluşturuldu ve öğrenci sınfı çağrıldı
print(nesne.ad+" "+nesne.soyad)
nesne.yazdir() # nesne üzerinden yazdır fonksiyonu çağırılarak da yazırılır

print("Ortalama :",nesne.ortalama(40,80))