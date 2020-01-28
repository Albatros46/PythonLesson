# if elif else döngüsü
print ("Python da ilk Projem :) ")
a=float(input("1.Sayıyı Giriniz :"))
b=int(input("2.Sayıyı Giriniz :"))
print("1-TOPLAMA")
print("2-ÇIKARMA")
print("3-ÇARPMA")
print("4-BÖLME")
c=int(input("Yapmak İstediğiniz İşlemi Seçiniz :"))
if c==1:
    print("Sayıların Topmaı :",a+b)
elif c==2:
    print("Sayıların Farkı :",a-b)
elif c==3:
    print("Sayıların Çarpımı :",a*b)
elif c==4:
    print("Sayıların Bölümü :",a/b)
else :print("BÖYLE BİR SEÇİM YOKTUR!..")



