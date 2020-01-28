# Iterators - Yinelemeler veya Tekrarlamalar
liste=[1,2,3,4,5]
iterasyon=iter(liste) #iter fonksiyonu ile nesneyi tanımlıyoruz
print(next(iterasyon)) # next komutu sonraki elemanı getirir
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
#print(next(iterasyon)) # son eleman olmadığı için hata verecektir
liste2=["Bekir","Serpil","Servet","Ahmet","Akif","Oğuz","Rukiye"]
aile=iter(liste2)
while True:
    try:
        print(next(aile))
    except StopIteration:
        print("Listenin Sonuna Gelindi")
        break
class teksayibul:
    def __iter__(self):
        self.sayi=1
        return self
    def __next__(self):
        sayi=self.sayi
        self.sayi+=2 # self yazılmaz ise 1 e 2 ekleyerek sadece 3 yazar
        return sayi
a=iter(teksayibul())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))