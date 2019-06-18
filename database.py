import sqlite3
from colorama import Fore, Back, Style
import time
from Nesneler import Personel
from myExcel import MyExcel

class Database():
    def __init__(self):
        self.create_connect()
    def __del__(self):
        self.close_connect()
    def create_connect(self):
        self.connect = sqlite3.connect("development.db")
        self.cursor = self.connect.cursor()
        self.create_personel_table()
        self.create_gorev_table()
        self.create_gorev_takip_table()

    def close_connect(self):
        self.connect.close()

    # Tabloları Oluşturmak
    def create_personel_table(self):
        query = "CREATE TABLE IF NOT EXISTS personel (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ad VARCHAR(255), soyad VARCHAR(255), yas INT(10), cinsiyet VARCHAR(50), gorev VARCHAR(255), baslama_tarihi VARCHAR(255))"
        self.cursor.execute(query)
        self.connect.commit()
    def create_gorev_table(self):
        query = "CREATE TABLE IF NOT EXISTS gorev (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ad VARCHAR(255), aciklamasi TEXT, gorev_tarihi VARCHAR(255), tekrarlanma INTEGER, mail_grubu INTEGER, created_date VARCHAR(255))"
        self.cursor.execute(query)
        self.connect.commit()
    def create_gorev_takip_table(self):
        query = "CREATE TABLE IF NOT EXISTS gorev_takip (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, gorev_id INTEGER, durumu INTEGER, created_date VARCHAR(255))"
        self.cursor.execute(query)
        self.connect.commit()

    # Personel İşlemleri
    def show_personel(self):
        query = "SELECT * FROM personel"
        self.cursor.execute(query)
        personeller = self.cursor.fetchall()
        print(Style.RESET_ALL)
        if (len(personeller) == "0"):
            print(Fore.RED + "Personeller Tablosu Boş.")
            print(Fore.RED + "Lütfen yeni personel giriniz.")
        else:
            for i in personeller:
                personel = Personel(i[1], i[2], i[3], i[4], i[5], i[6], i[0])
                print(Fore.GREEN + "---------------------------------")
                print(personel)
            Excel = MyExcel('personel-listesi.xlsx')
            Excel.create_personel_listesi(personeller)

        input("İşleme devam etmek için bir tuşa basın...")
    def save_personel(self, personel):
        query = "INSERT INTO 'personel' VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (personel.ad, personel.soyad, personel.yas, personel.cinsiyet, personel.pozisyon, personel.bTarihi))
        self.connect.commit()
        print(Fore.GREEN + "Personel Kaydı Oluşturulmuştur.")
        time.sleep(5)
    def delete_personel(self, id):
        query = "DELETE FROM personel WHERE id = ?"
        self.cursor.execute(query, id)
        self.connect.commit()
        print(Fore.YELLOW + "Personel başarılı bir şekilde silindi.")
        time.sleep(5)
