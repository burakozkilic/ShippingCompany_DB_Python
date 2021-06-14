
import sqlite3
con = sqlite3.connect('Nakliye_Sirketi.db')
cur = con.cursor()

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (1,'Mehmet','Karaman','E','Sultabeyliği Dörtyol Mah.','İstanbul','Türkiye',31405,'05225485887'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (2,'Burak','Özkılıç','E','Mehmet Akif Mah.','Bursa','Türkiye',31478,'05389575966'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (3,'Selami','Cuma','E','Orhan Gazi Mah.','Sivas','Türkiye',30578,'05386845461'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (4,'Adem','Türk','E','Atatürk Mah.','Hakkari','Türkiye',34320,'05318407823'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (5,'Ceylan','Çakmak','K','Linden Mah','Berlin','Almanya',30132,'05499892963'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (6,'İrem','Keskin','K','Unter Mah.','Berlin','Almanya',32330,'05264132369'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (7,'Hüseyin','Kurt','E','Orhangazi Mah.','Bursa','Türkiye',33301,'05730900166'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (8,'Burak','Mermer','E','Süleyman Mah.','İstanbul','Türkiye',31323,'05765683523'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (9,'Sude','Naz','K','Alınteri Mah.','Hakkari','Tükiye',32323,'05090933525'); 
    ''')

cur.execute('''
        INSERT INTO Alici (Alici_ID,Alici_Adi,Alici_Soyadi,Cinsiyet,Alici_Adres,Alici_Sehir,Alici_Ulke,Posta_Kodu,Telefon_Numarası)
        VALUES (10,'Meltem','Bor','K','Kıbrıslılar Mah.','Sivas','Türkiye',34113,'05525847624'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (1,'Kütahya','Altıntaş'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (2,'Sivas','Altınyayla'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (3,'Aydın','Bozdoğan'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (4,'Kocaeli','Gebze'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (5,'İstanbul','Çekmeköy'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (6,'Denizli','Çal'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (7,'Karaman','Başyayla'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (8,'Konya','Ahırlı'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (9,'Zonguldak','Gökçebey'); 
    ''')

cur.execute('''
        INSERT INTO Depo (Depo_ID,Sehir,Ilce)
        VALUES (10,'Berlin','Mitte'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (1,'Evyap','Kütahya','Altıntaş'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (2,'Arçelik','Samsun','Alaçam'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (3,'Bosh','Mersin','Erdemli'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (4,'Ford','Ağrı','Diyadin'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (5,'Mercedes Benz','İstanbul','Kadıköy'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (6,'Vestel','Gaziantep','Araban'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (7,'Apple','Tokat','Pazar'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (8,'Samsung','Adana','Ceyhan'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (9,'Fiat','Rize','Çayeli'); 
    ''')

cur.execute('''
        INSERT INTO Firma (Firma_ID,Isim,Bulundugu_Sehir,Bulundugu_Ilce)
        VALUES (10,'Porsche','Berlin','Den'); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (1,'Mercedes','2001-12-21T00:00:00',1902034325,1); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (2,'Ford','2005-01-20T00:00:00',1902034325,2); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (3,'İveco','2018-03-24T00:00:00',1420440027,3); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (4,'Man','2019-03-27T00:00:00',1153300371,4); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (5,'Scania','2009-04-25T00:00:00',1431305762,5); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (6,'BMC','2021-11-21T00:00:00',1610317424,6); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (7,'Volvo','2005-12-31T00:00:00',1162323262,7); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (8,'Daf','1997-10-01T00:00:00',1390490639,8); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (9,'Volkswagen','2019-11-17T00:00:00',1726504210,9); 
    ''')

cur.execute('''
        INSERT INTO Kamyon (Kamyon_ID,Marka,Alindigi_Yil,Sase_No,Kasa_Turu_ID)
        VALUES (10,'Renault','2013-07-16T00:00:00',1961574808,10); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (1,'Soğutmalı Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (2,'Isıtmalı Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (3,'Açık Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (4,'Kapalı Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (5,'XXL Uzun Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (6,'Meşrubat Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (7,'Damperli Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (8,'Branda Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (9,'Saç Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kasa_Turu (Kasa_Turu_ID,Kasa_Turleri)
        VALUES (10,'Panel Kasa'); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (1,'Emir','Ermiş','Erzincan',4000,19); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (2,'Ahmet','Aksu','Sivas',3500,20); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (3,'Selami','Kurt','Erzincan',2800,39); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (4,'Mehmet','Gür','Tekirdağ',3250,41); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (5,'Yaşar','Ulu','Kastamonu',2250,27); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (6,'Arda','Tel','Sinop',5120,54); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (7,'Süleyman','Kemer','Osmaniye',1925,22); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (8,'Ayşe','Şerafettin','Şırnak',9218,56); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (9,'Lale','Pat','Ankara',2250,21); 
    ''')

cur.execute('''
        INSERT INTO Kurye (Kurye_ID,Ad,Soyad,Memleket,Maas,Yasi)
        VALUES (10,'Neriman','Güzel','Ankara',4128,35); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (1,1,1,1,1,2,1,1,1); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (2,2,2,2,2,3,2,2,2); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (3,3,3,3,3,4,3,3,3); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (4,4,4,4,4,5,4,4,4); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (5,5,5,5,5,6,5,5,5); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (6,6,6,6,6,7,6,6,6); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (7,7,7,7,7,8,7,7,7); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (8,8,8,8,8,9,8,8,8); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (9,9,9,9,9,10,9,9,9); 
    ''')

cur.execute('''
        INSERT INTO Paket (Paket_ID,Paket_Tipi_ID,Tasindigi_Kamyon,Ulastiran_Kurye,Bulundugu_Depo,Gidilecek_Depo,Gonderen_Firma,İcerik_Turu_ID,Alici_ID)
        VALUES (10,10,10,10,10,1,10,10,10); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (1,'Elektronik'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (2,'Gıda'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (3,'Ziynet'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (4,'Tıbbi'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (5,'Hayvan'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (6,'Kimyasal Madde'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (7,'Cam'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (8,'Tekstil'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (9,'Teknolojik'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Icerigi (Paket_Icerik_Turu_ID,Paket_Icerigi)
        VALUES (10,'Hammadde'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (1,'Çuval'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (2,'Poşet'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (3,'Kutu'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (4,'Zarf'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (5,'Bavul'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (6,'Kafes'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (7,'Ambalaj'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (8,'Varil'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (9,'Medikal Dolap'); 
    ''')

cur.execute('''
        INSERT INTO Paket_Tipi (Paket_Tipi_ID,Paket_Tipi)
        VALUES (10,'Tanker'); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (1,'Kemal','Sancak',38,'Hakkari',358832,3444,1); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (2,'Zeynep','Bor',31,'Erzincan',203838,4238,2); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (3,'Emre','Taş',41,'Kıbrıs',787604,3532,3); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (4,'Güliz','Ak',21,'Antalya',601132,2886,9); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (5,'Hüseyin','Ermiş',44,'İzmir',716773,4353,4); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (6,'Recep','Kaya',37,'Çanakkale',533155,2685,5); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (7,'Meltem','Pınar',41,'Edirne',847077,4858,8); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (8,'Emine','Taş',30,'Eskişehir',116108,3020,7); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (9,'Yaşar','Ermiş',48,'İstanbul',878108,2286,10); 
    ''')

cur.execute('''
        INSERT INTO Sofor (Sofor_ID,Ad,Soyad,Yas,Memleket,Sicil_No,Maas,Kullandigi_Kamyon)
        VALUES (10,'Sevil','Ece',45,'İstanbul',702280,2419,6); 
    ''')
con.commit()
con.close()