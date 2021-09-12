import sqlite3


class DB:

    conn = None
    pathDB = None
    cur = None

    def __init__(self, pathDB) -> None:
        if pathDB == None:
            print('Path to SQLite cannot be Null')
        else:
            self.pathDB = pathDB
            self.connect_db()
            if self.conn == None:
                print('Cannot to connect SQLite')

    def connect_db(self):
        self.conn = sqlite3.connect(self.pathDB)
        self.cur = self.conn.cursor()
        # self.conn.set_trace_callback(print)

    def insert(self, id, name, birthday):
        query = 'INSERT INTO people (id,name,birthday) VALUES (?,?,?)'
        self.query(query, (id, name, birthday))

    def update(self, id, name, birthday):
        query = "UPDATE people set name= ?, birthday= ? where id = ?"
        self.query(query, (name, birthday, id))

    def select(self, column, value):
        if self.conn != None:
            query = """SELECT * FROM people where """ + column + """ = :value"""
            self.cur.execute(query, {'value': value})
            return self.cur.fetchall()
        else:
            print('Cannot select data because cannot connect to DB')
            return None

    def delete(self, column, value):
        query = """DELETE FROM people WHERE """ + column + """ = ?"""
        self.query(query, (str(value)))

    def query(self, query, parameter=None):
        if self.conn != None:
            self.cur.execute(query, parameter)

            self.conn.commit()
        else:
            print('Cannot connect to DB')

    def closeDB(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB('people.db')
    # db.insert(2, 'chinh', 1999)
    # db.delete('id', 1)
    # db.update(1, 'chinh 2', 2000)
    # print(db.select('id', 1))
