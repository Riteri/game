import psycopg2 as ps

conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
cur = conn.cursor()

cur.execute("CREATE TABLE slowa_do_gry(zwierzeta varchar , ubrania varchar, czesci_ciala varchar, rodzaj_sportu varchar );")

cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('PAJAK','SUKIENKA', 'KOLANO', 'BADMINTON')")
cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('ZYRAFA','KOSZULA', 'STOPA', 'AKROBATYKA')")
cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('POPUGA','KAPELUSZ', 'SZYJA', 'SZACHY')")
cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('SLIMAK','SPODNICA', 'BRZUCH', 'BASEBALL')")
cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('CHOMIK','SKARPETY', 'PRZEDRAMIENIE', 'SIATKOWKA')")
cur.execute("INSERT INTO slowa_do_gry (zwierzeta, ubrania,czesci_ciala,rodzaj_sportu) VALUES ('PANTERA','KRAWAT', 'WARGI', 'HOKEJ')")




conn.commit()
cur.close()
conn.close()

