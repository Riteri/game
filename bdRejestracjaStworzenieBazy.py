import psycopg2 as ps

class DbRejestracja:
    def db_rejestracja(self):
        self.conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.cur =self.conn.cursor()

        self.cur.execute("CREATE TABLE bdGraczy(nick varchar , email varchar , plec varchar , haslo varchar , sciezka_do_avataru varchar );")


        self.conn.commit()
        self.cur.close()
        self.conn.close()


db = DbRejestracja()
db.db_rejestracja()