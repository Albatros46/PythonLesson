# Polymorphism (Çok Biçimlilik)
# Bazı sınıflarda ortak fonk bulunabiir bu fonk sınıfı tek tek oluşturulmadan çağıralabilir
class kedi:
    def ses(self):
        print("Miyavvvv")

class kopek:
    def ses(self):
        print("Hav Hav")

class kus:
    def ses(self):
        print("Cik Cik")

def hayvansesi(hayvan):
    hayvan.ses()

ke = kedi()
ko = kopek()
ku = kus()

hayvansesi(ke)
hayvansesi(ko)
hayvansesi(ku)
