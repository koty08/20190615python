import pymysql

#커넥션 개체 생성 함수

def conn_db():
    conn = pymysql.connect(host='localhost',user='root',
    password='qwer1234',db='test',charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    return conn

#테이블 생성함수
def create_table():
    conn=conn_db()
    c=conn.cursor()
    c.execute('''create table if not exists music(
        rank int NOT NULL,
        link varchar(255),
        name varchar(255),
        artist varchar(30)
        )''')
    conn.commit()
    conn.close()

#데이터 입력 함수
def insert_music(items):
    conn=conn_db()
    c=conn.cursor()
    sql='insert into music values(%s,%s,%s,%s)'
    c.executemany(sql, items) 
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_music():
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM music")
    items=c.fetchall()
    conn.close()
    return items