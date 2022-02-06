import psycopg2 as ps

class DbPoints:
    def points(self):
        """
            :description: creation database -  points
        """
        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "CREATE TABLE points(nick varchar , points varchar );")

        self.conn.commit()
        self.cur.close()
        self.conn.close()

db= DbPoints()
db.points()
