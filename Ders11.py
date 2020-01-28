# Constructer (yapıcı) Fonksiyonlar
class cokgen:
    def __init__(self,g,y):
        self.genislik=g
        self.yukseklik=y
    def alan(self):
        return self.genislik*self.yukseklik
dikdortgen=cokgen(20,10)
print(dikdortgen.genislik ,",",dikdortgen.yukseklik)
print(dikdortgen.alan())