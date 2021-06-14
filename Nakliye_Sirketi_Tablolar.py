
import sqlite3
con = sqlite3.connect('Nakliye_Sirketi.db')
cur = con.cursor()


cur.execute('''
    CREATE TABLE Alici
    (
        Alici_ID num PRIMARY KEY,
        Alici_Adi text,
        Alici_Soyadi text,
        Cinsiyet text,
        Alici_Adres text,
        Alici_Sehir text,
        Alici_Ulke text,
        Posta_Kodu num,
        Telefon_Numarası num
    )
''')

cur.execute('''
    CREATE TABLE Depo
    (
        Depo_ID num PRIMARY KEY,
        Sehir text,
        Ilce text
    )
''')

cur.execute('''
    CREATE TABLE Firma
    (
        Firma_ID num PRIMARY KEY,
        Isim text,
        Bulundugu_Sehir text,
        Bulundugu_Ilce text
    )
''')

cur.execute('''
    CREATE TABLE Kamyon
    (
        Kamyon_ID num PRIMARY KEY,
        Marka text,
        Alindigi_Yil text,
        Sase_No num,
        Kasa_Turu_ID num NOT NULL,
        FOREIGN KEY(Kasa_Turu_ID) REFERENCES Kasa_Turu(Kasa_Turu_ID)
    )
''')

cur.execute('''
    CREATE TABLE Kasa_Turu
    (
        Kasa_Turu_ID num PRIMARY KEY,
        Kasa_Turleri text
    )
''')

cur.execute('''
    CREATE TABLE Kurye
    (
        Kurye_ID num PRIMARY KEY,
        Ad text,
        Soyad text,
        Memleket text,
        Maas num,
        Yasi num
    )
''')

cur.execute('''
    CREATE TABLE Paket
    (
        Paket_ID num PRIMARY KEY,
        Paket_Tipi_ID num NOT NULL,
        Tasindigi_Kamyon num NOT NULL,
        Ulastiran_Kurye num NOT NULL,
        Bulundugu_Depo num NOT NULL,
        Gidilecek_Depo num NOT NULL,
        Gonderen_Firma num NOT NULL,
        İcerik_Turu_ID num NOT NULL,
        Alici_ID num NOT NULL,
        FOREIGN KEY(Paket_Tipi_ID) REFERENCES Paket_Tipi(Paket_Tipi_ID),
        FOREIGN KEY(Tasindigi_Kamyon) REFERENCES Kamyon(Kamyon_ID),
        FOREIGN KEY(Ulastiran_Kurye) REFERENCES Kurye(Kurye_ID),
        FOREIGN KEY(Bulundugu_Depo) REFERENCES Depo(Depo_ID),
        FOREIGN KEY(Gidilecek_Depo) REFERENCES Depo(Depo_ID),
        FOREIGN KEY(Gonderen_Firma) REFERENCES Firma(Firma_ID),
        FOREIGN KEY(İcerik_Turu_ID) REFERENCES Paket_Icerigi(Paket_Icerik_Turu_ID),
        FOREIGN KEY(Alici_ID) REFERENCES Alici(Alici_ID)          
    )
''')

cur.execute('''
    CREATE TABLE Paket_Icerigi
    (
        Paket_Icerik_Turu_ID num PRIMARY KEY,
        Paket_Icerigi text
    )
''')

cur.execute('''
    CREATE TABLE Paket_Tipi
    (
        Paket_Tipi_ID num PRIMARY KEY,
        Paket_Tipi text
    )
''')

cur.execute('''
    CREATE TABLE Sofor
    (
        Sofor_ID num PRIMARY KEY,
        Ad text,
        Soyad text,
        Yas num,
        Memleket text,
        Sicil_No num,
        Maas num,
        Kullandigi_Kamyon num NOT NULL,
        FOREIGN KEY(Kullandigi_Kamyon) REFERENCES Kamyon(Kamyon_ID)
    )
''')