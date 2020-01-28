# Global, Local ve nolocal değişkenler
x=2 # global bir değişkendir
def fonksiyon():
    x=5 #local değişken oldu sadece fonksyion içinde kullanılan değişkendir
    print("İç Değer:",x)
fonksiyon()

print("Dışarı :",x) # global olan değişken çağırıldı

sayi=10 #global değişken
def f2():
    global sayi # gloabl değişkeni kullanmak için izin aldık
    sayi=sayi*2
    print("sayi değeri :",sayi)
f2()


