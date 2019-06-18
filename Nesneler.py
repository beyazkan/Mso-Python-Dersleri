
class Personel():
    def __init__(self, ad, soyad, yas, cinsiyet, pozisyon, bTarihi, id_value = "NULL"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.pozisyon = pozisyon
        self.bTarihi = bTarihi
        self.id = id_value

    def __str__(self):
        return "Personel Bilgileri\nNumarası: {}\nAdı: {}\nSoyadı: {}\nYaşı: {}\nCinsiyeti: {}\nPozisyonu: {}\nBaşlama Tarihi: {}".format(self.id, self.ad, self.soyad, self.yas, self.cinsiyet, self.pozisyon, self.bTarihi)