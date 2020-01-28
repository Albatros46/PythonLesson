# SET Küme Kavramı
kume={1,2,3,5,7,9,4}
print(kume)
#Kümenin diziden farkı tekrarlayan elemana izin vermez
kume2={1,2,3,4,5,1,2,3,4,5,}
print(kume2)

kume3=set("Ben bir metinim, bir string ifade")
print(kume3)
kume4={"Ben bir metinim, bir string ifade"}
print(kume4)
# Kümelerin farkları ve toplamı da yapılabilir
print(kume2.difference(kume3))