# Ananonim Fonksiyonlar ve Lampda kullanımı
# fonksiyon_ismi=lampda degisken:islem

ikikat= lambda x:x*2
print(ikikat(5))

liste=[1,2,3,4,5,6,7,8,9]
yeni_liste=list(filter(lambda x:(x%2==1),liste)) # liste dizinindeki sayıları lamda ile 2 ye böldürüp kalan 1 verenleri yani tek sayıları
                                                #yeni listede yazdırdı x% x mod anlamında
print(yeni_liste)

yeni_liste2 = list(map(lambda x:(x*3),liste))#liste elemanındaki sayıların 3  katını almasını istedik
print(yeni_liste2)