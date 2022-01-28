import psycopg2 as ps

conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
cur = conn.cursor()

cur.execute("CREATE TABLE slowa_do_gry(Animals varchar , Clothes varchar, body_parts varchar, kind_of_sport varchar );")

cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('SPIDER','DRESS', 'KNEE', 'BADMINTON')")
cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('GIRAFFE','SHIRT', 'FOOT', 'ACROBATICS')")
cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('PARROT','HAT', 'NECK', 'CHESS')")
cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('SNAIL','SKIRT', 'BELLY', 'BASEBALL')")
cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('HAMSTER','SOCKS', 'shoulders', 'VOLLEYBALL')")
cur.execute("INSERT INTO slowa_do_gry (Animals, Clothes,body_parts,kind_of_sport) VALUES ('LEOPARD','NECKTIE', 'LIPS', 'HOCKEY')")




conn.commit()
cur.close()
conn.close()

