import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''

    SELECT MAX(Yasi) AS EnBuyukYas FROM Kurye
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)