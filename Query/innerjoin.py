import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''

    SELECT sofor.Ad, Kamyon.Marka
    FROM Sofor
    INNER JOIN Kamyon
    ON Kamyon.Kamyon_ID = Sofor_ID
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)