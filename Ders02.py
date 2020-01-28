# For döngüsü
for x in range(10): # 0 dan 9 a kadar döndürecek range nokta koyulacak deger
    print(x)

for y in range(3,9): # RANGE ile aralıkta belirtilebilir
    print(y)

for z in range(20,40,2): # 20 ile 40 arasındaki sayıları 2 şer artırır
    print(z)

for k in reversed(range(10,20)): # tersine döngü kurmak için Reversed kullanılır.
    print(k) #20 den 10 a döndürür.

for c in "PYTHON DA DÖNGÜLER SÜPER": #String ifadelerde döngüler
    print(c)

a=[2,3,4,5,6,7,8] #örnek dizi
for b in a:
    print(b)
# While döngüsü
x=0 #x i sıfırladık
while x<15: #x 15 den küçük olana kadar Merhaba SERVET yazacak
    print("%s.Merhaba SERVET"%(x))
    x+=1
    if (x==10): # fakat x 10 a geldiğinde döngü kapanacak
        break