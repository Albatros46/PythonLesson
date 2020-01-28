#ÇOK BOYUTLU DİZİLER
m1=[[2,0,3],
   [4,5,2],
   [7,9,1]]
print(m1[0])
for i in range(3):
    print(m1[i]) # matris alt alta yazdırdık
m2=[[11,21,31], #ikinci matris yazdırıldı
    [41,51,61],
    [22,32,42]]
for i in range(3):
    print(m2[i])
    m3 = [[0, 0, 0],  # m3 matrisi tanımlandı
          [0, 0, 0]
          [0, 0, 0]]
for i in range(3):
   for j in range(3): # iki matris toplayarak sonucu başka matris e yazdırma işlemi
        m3[i][j] = m1[i][j] + m2[i][j]
print()
 for i in range(3):
    print(m3[i])
