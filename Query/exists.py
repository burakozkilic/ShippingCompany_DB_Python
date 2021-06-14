import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''
    SELECT * FROM Paket WHERE EXISTS
    (SELECT Sehir FROM Depo WHERE Paket.Bulundugu_Depo
    = Depo.Depo_ID AND Depo.Sehir='İstanbul')
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)