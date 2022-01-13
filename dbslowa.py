import random
import psycopg2 as ps



class DbRand :


    def dbrand(self):
        self.conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.rand =self.conn.cursor()
        self.random_thems = random.choice(['zwierzęta', 'ubrania', 'części_ciała', 'rodzaj_sportu'])
        # print(self.random_thems)

        self.rand.execute("SELECT "+ self.random_thems +" FROM slowa_do_gry")
        self.outputslowaisdb = self.rand.fetchall()
        # print(self.random_thems + str(self.outputslowaisdb))


        self.randomslowa = random.choice(self.outputslowaisdb)

        # убрал все лишнее потому что объект был типа tuple  и в окне игры не считовалось количество букв

        self.slowojoin = "".join(map(''.join, self.randomslowa))

        print(self.slowojoin)

        self.conn.close()
        self.rand.close()

db = DbRand()



