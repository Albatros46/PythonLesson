# Dosya işlemleri
dosya=open("Ders16.txt",mode='w',encoding='utf-8') # a modunda ise her çalıştığında üzerine yazar
# açıktık    adı     W=write(yazma)    utf-8=türkçe karakter desteği
# projenin çalıştığı dizin varsayılan olarak belirlenir istenirse yol belirtilir
# c:\deneme.txt gibi
# w-write modülüdür. dosya yoksa yeniden oluşturulur varsa da içi silinir yeniden yazılır
# a-append üzerine yazma modu
# r-read modu okumak modudur
# utf-8 karakter kodlama (türkçe kararkter tanoması için)
dosya.write("Servet AKÇADAĞ\n") # yazma işlemi
dosya.write("KAHRAMANMARAŞ\n") # yazma işlemi
dosya.close()
dosya=open("Ders16.txt",mode='r',encoding='utf-8') # Dosyayı okumak için açtık
print(dosya.read())
