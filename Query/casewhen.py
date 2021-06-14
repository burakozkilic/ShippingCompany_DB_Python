import sqlite3
baglanti =sqlite3.connect('Nakliye_Sirketi.db')
imlec = baglanti.cursor()

imlec.execute('''
    SELECT Paket_ID,
    CASE
        WHEN Bulundugu_Depo = 1 THEN 'Kütahya Deposu'
        WHEN Bulundugu_Depo = 2 THEN 'Sivas Deposu'
        WHEN Bulundugu_Depo = 3 THEN 'Aydın Deposu'
        WHEN Bulundugu_Depo = 4 THEN 'Kocaeli Deposu'
        WHEN Bulundugu_Depo = 5 THEN 'İstanbul Deposu'
        WHEN Bulundugu_Depo = 6 THEN 'Denizli Deposu'
        WHEN Bulundugu_Depo = 7 THEN 'Karaman Deposu'
        WHEN Bulundugu_Depo = 8 THEN 'Konya Deposu'
        WHEN Bulundugu_Depo = 9 THEN 'Zonguldak Deposu'
        WHEN Bulundugu_Depo = 10 THEN 'Berlin Deposu'
    END AS Depo_Ismi FROM Paket
         
    
''')

rows = imlec.fetchall()

for row in rows:
    print(row)