import sqlite3

class DatabaseManager(object):
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, query, arg):
        #print query, arg
        data = self.cur.execute(query, arg)
        
        #self.conn.commit()
        #row = data.fetchall()
        return data

    def __del__(self):
        self.conn.close()