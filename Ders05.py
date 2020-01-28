#Dictionary Kullanımı
dict={1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi"}
print(dict[3]) #Dict kullanımı
# Kullanıcıdan iki basamaklı sayı isteyip yazı olarak değiştirmek
dict_a={1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz",0:"Sıfır"}
dict_b={1:"On",2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan"}
sayi=print(input("İki Basamaklı Bir Sayı Giriniz :"))
birler=int(sayi[1]) # Sayının Birler Basamağı 1. indis
onlar=int(sayi[0]) # Sayınnın onlar basamağı 0. ıncı indis
print(dict_b[onlar]) + (dict_a[birler])