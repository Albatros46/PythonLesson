# Decorators
# Python da decorator lar argüman olarak fonksiyon alıp
# sonuçta yine fonksiyon döndüren fonksiyonlardır
def linkyap(f):
    def yaz():
        return "<a href='http://www."+f()+".com'>Link</a>"
    return yaz
def adres():
    return "google"
a=linkyap(adres)
print(a())
@linkyap # fonksiyonu decoration a bağlıyoruz
def adr():
    return "python"
print(adr())