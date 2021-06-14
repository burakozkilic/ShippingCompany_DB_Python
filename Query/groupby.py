import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''
    SELECT Alici_Sehir, COUNT(*) FROM Alici GROUP BY Alici_Sehir
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)