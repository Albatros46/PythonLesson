# Diziler
dizi =[0,1,2,3,4,5,6,7,8,9]
dizi[0]=5 #dizinin 0 ıncı elemanı değiştirilerek yerine 5 yazdırıldı
print (dizi)
print(dizi[0]) #sadece 0. elemanını yazdır
print(dizi[0:5]) #Python da dizi istediğin yerden bölebilirsin
                # dizinin 0 ıncı elemanından 5. elemanına kadar yazar
print(dizi[3:7]) #dizi 3. elemandan  7. eleman a kadar yazırdı
print(dizi[:3]) # 0 ıncı indisten 3. elemana kadar yazdırdı
print(dizi[4:]) # son elemandan 4. eleman a kadar
print(dizi[-1]) #dizi döndürüldü son elemanı yazdırdı
print(dizi[-3]) # sondan üçünccü elemanı yazdırdı
print(len(dizi)) # dizinin eleman sayısını belirtir
#--------------------------------------------------------
#string dizinler tanımlama
sdizi=["Elma","Armut","Ceviz","Muz"]
print(sdizi[2]) #dizinin 2. elenanı
sdizi.append("üzüm") #dizinin arkasına eleman eklenir
print(sdizi)
del sdizi[1] #indisli elemanı siliniyor
print(sdizi)
sdizi.remove("Ceviz") #dizi elemanı biliyorsak silme işlemi
print(sdizi)

sdizi.pop(2) #indis numarası ile silme işlemi
print(sdizi)
sdizi += ["armut", "üzüm", "portakal"]  # += işareti ile iki dizi toplanabilir birleştirilebilir

sdizi*=2 #dizi içerisinde çarpar bütün elemanı 2 ile çarpıyor
print(sdizi)
#-------------------------------------
sayilar=[21,12,45,56,78,34,89,93,21,21,21,21]
sayilar.sort()
print(sayilar) #sayıları küçükten büyüğe sıraladı
sayilar.reverse() # küçüktek büyüğe sıralı diziyi ters çevirdi
print(sayilar) #diziyi şimdi de büyükten küçüğe yazdırdı
sayilar.count(21)
print(sayilar.count(21)) #21 elemanı dizide kaç defa tekrar etmiş
sayilar.clear()#dizi içeriği temizlendi
print(sayilar)
sayilar.insert(0,38) # 0 ıncı elemana 12 ekledi
sayilar.insert(1,54) # 1 inci elemana 54 ekledi
sayilar.insert(1,32) # 1 inci elemanın arasına 32 ekledi
print(sayilar)
#----ÇOK BOYUTLU DİZİLER--------
matris=[[1,3,6],[4,12,21],[11,32,41]] # üç boyutlu dizi
print(matris)
#1,3,6
#4,12,21
#11,32,41 şeklinde
print(matris[0])# 0 ıncı indis elemanları
print(matris[2][2]) # 2 indisli dizinin 2. indisli elemanı
