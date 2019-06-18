from clearFunction import clear
from time import sleep
import colorama
from colorama import Fore, Back, Style
import database
from Nesneler import Personel
from myMail import MyMail


colorama.init(autoreset=True)

veritabani = database.Database()
personelListesi = []

def anaMenu():
    clear()
    print(Fore.RED + "---------------   Proje-1'e Hoşgeldiniz...   ---------------")
    print("Şirketinizde bulunan personellerin" \
        " kaydını tutan bir program.\n")
    print(Back.WHITE + Fore.BLACK + "İşlem Seçenekleri;")
    print("1. Yeni Personel")
    print("2. Personel Bilgisi")
    print("3. Personel Sil")
    print("4. Programı Sonlandır.")

def kayit():
    print(Fore.RED + "Kaydını gerçekleştireceğiniz personel bilgilerini giriniz.")
    ad = input("Adı: ")
    soyad = input("Soyadı: ")
    yas = int(input("Yaşı: "))
    cinsiyet = input("Cinsiyeti (Örn. Erkek - Kadın): ")
    pozisyon = input("Pozisyon: ")
    bTarihi = input("Başlama Tarihi (Örn: 12.02.2019): ")
    personel = Personel(ad, soyad, yas, cinsiyet, pozisyon, bTarihi)
    veritabani.save_personel(personel)

def goster():
    veritabani.show_personel()
    myMail = MyMail("smtp.gmail.com", 587, "mail_address", "Password")
    myMail.toMail("to_address")
    myMail.message_generate("Merhaba", "Bu bir test mailidir.")
    myMail.attachment_file("personel-listesi.xlsx", "output\\")
    myMail.send_mail()

def sil():
    id_value = input(Fore.RED + "Silmek istediğiniz personelin numarasını yazın: ")
    veritabani.delete_personel(id_value)

while (True):
    anaMenu()
    veri = input(Fore.CYAN + "Lütfen yapmak istediğiniz işlemi seçin: ")
    if(veri == '4'):
        print(Fore.RED + "Program başarılı bir şekilde sonlandırıldı.")
        break

    elif(veri == '1'):
        kayit()

    elif(veri == '2'):
        goster()

    elif(veri == '3'):
        sil()

    else:
        clear()
        print(Fore.YELLOW + "Bu seçenek henüz hazır değil.")
        print(Fore.YELLOW + "Lütfen daha sonra deneyiniz.")
        sleep(3)