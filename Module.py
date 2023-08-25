import pymysql
from datetime import datetime


class DataBase:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect_to_db(self):
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        return conn

    def execute_query(self, query):
        conn = self.connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def get_first_result(self, send_query):
        query_result = self.execute_query(send_query)
        if query_result:
            return query_result[0]
        return None


class GetTime:
    def __init__(self):
        self.nowtime = datetime.now()

    def sendtime(self):
        h = self.nowtime.hour
        m = self.nowtime.minute
        s = self.nowtime.second

        time = f"{h}시 {m}분 {s}초"

        return time


if __name__ == "__main__":
    host = '192.168.38.122'
    user = 'admin'
    password = 'happy1003!'
    db = 'Hackathon'

    database = DataBase(host, user, password, db)
    send_query = "SELECT * FROM web where name='강서구 지하차도' order by id desc"
    check_grade = database.get_first_result(send_query) # 실시간 지하차도 등급 조회 변수

    nowtime = datetime.now()
    time = GetTime().sendtime()

