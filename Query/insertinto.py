import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''
    INSERT INTO Firma (Isim,Bulundugu_Sehir,Bulundugu_Ilce)
    VALUES ('Apple','New York', 'California')
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)