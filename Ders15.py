#  Map, filter, reduce fonksiyonları
# dizilerde ve dizi elemanlarına değişiklik yapmaya yarar
# map bütün dizi elemenlarında değişiklik yapmak için kullanılır
liste =[2,5,6,7,9] # döngü kullanamdan map ile bütün dizi elemanlarının kaersini aldık
yeni_liste=list(map(lambda  x:x**2,liste))
print(yeni_liste)

def ikikat(x):
    return x*2
def yari(x):
    return x/2
fonk=[ikikat,yari]
for i in range(5):
    deger=list(map(lambda x:x(i),fonk))
    print(deger)

# filter belirleidğimiz şartlara göre listeleme yapar
liste=[1,2,5,6,9,16,25,27,45,46]
uce_bolunenler=list(map(lambda x:x%3,liste))
print(uce_bolunenler) # 3 e bölümünden kalanları listeler
uce_bolunenler=list(map(lambda x:x%3==0,liste))
print(uce_bolunenler) # True - False degerler verir

# reduce dizi/liste elemanlarının toplanması, çarpılması işlemlerinde kullanılır
from functools import reduce # reduce yi kütüphanden çağırdık 
toplam=reduce(lambda x,y:x+y,liste)
print(toplam)