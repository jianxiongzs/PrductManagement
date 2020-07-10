import pymysql

class Database():
    def __init__(self, db):
        self.host = db['host']
        self.user = db['user']
        self.passwd = db['passwd']
        self.database = db['database']
        self.conn = None
        self.cursor = None
    
    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user,
                                    passwd=self.passwd, database=self.database,
                                    charset='utf8'
                    )
        self.cursor = self.conn.cursor()

    def select(self,sql,param=None):
        self.cursor.execute(sql, param)
        result = self.cursor.fetchall()
        return result

    def insert(self, sql, param=None):
        try:
            self.cursor.execute(sql, param)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

        return self.cursor.rowcount

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
