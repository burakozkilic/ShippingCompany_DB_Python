import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''
    SELECT * FROM Alici WHERE Cinsiyet='K' OR Alici_Sehir='İstanbul'
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)