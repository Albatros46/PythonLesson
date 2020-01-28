# Generators - Üreteçler
# adım adım yapılacak işlemler için kullanılır
def uretec():
    sayi=0
    print(sayi,". adım")
    yield sayi # yield özel bir döndürme değimidir return yerine kullanılır
    sayi+=1
    print(sayi, ". adım")
    sayi += 1
    print(sayi, ". adım")
    sayi += 1
    print(sayi, ". adım")
a=uretec()
next(a)
next(a)
next(a)
#next(a) stopitration hatası verir
b=uretec()
for x in b:
    print(x)

