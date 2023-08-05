import psycopg2

class db_info:
    database="dvm_db"
    user="manager"
    password="manager"
    host="192.168.0.7"
    port="5432"


class db_conn:
    conn = None
    cur = None

    def connect(self):
        # 데이터베이스 연결 설정
        self.conn = psycopg2.connect(database=db_info.database, user=db_info.user, password=db_info.password, host=db_info.host, port=db_info.port)
    
    def commit(self):
        self.conn.commit()

    def execute(self, execute_command):
        # 커서 생성
        self.cur = self.conn.cursor()

        # SQL 구문 실행
        self.cur.execute(execute_command)
        
        result = self.cur.fetchall()

        # 커서 제거
        self.cur.close()
        
        # return output
        return result

    def close(self):
        # 연결 종료
        self.conn.close()
        self.conn = None


# 데이터베이스 연결 설정
#conn = psycopg2.connect(database=db_info.database, user=db_info.user, password=db_info.password, host=db_info.host, port=db_info.port)

 # 커서 생성
#cur = conn.cursor()

# SQL 구문 실행
#cur.execute("select * from deployment;")
#cur.execute("INSERT INTO users (name, email, birth_date) VALUES (%s, %s, %s)", ('John Doe', 'john@example.com', date(1980, 1, 1)))

# result = cur.fetchall()

# print(result)

# for row in result:
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print(row[3])
#     print(row[4])
#     print(row[5])

# 변경사항 커밋
#conn.commit()

# 연결 종료
# cur.close()
# conn.close()