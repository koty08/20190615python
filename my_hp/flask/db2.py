import pymysql

#커넥션 개체 생성 함수

def conn_db():
    conn = pymysql.connect(host='localhost',user='root',
    password='ty0201',db='test',charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    return conn

#테이블 생성함수
def create_table():
    conn=conn_db()
    c=conn.cursor()
    c.execute('''create table if not exists music2(
        link varchar(200),
        artist varchar(100),
        genre varchar(100),
        date varchar(100),
        company varchar(100)
        )''')
    conn.commit()
    conn.close()

#데이터 입력 함수
def insert_music(items):
    conn=conn_db()
    c=conn.cursor()
    sql='insert into music2 values(%s,%s,%s,%s,%s)'
    c.executemany(sql, items) 
    conn.commit()
    conn.close()

#데이터한개 출력함수
def all_music(idx):
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM music2")
    items=c.fetchall()
    item = items[idx]
    conn.close()
    return item