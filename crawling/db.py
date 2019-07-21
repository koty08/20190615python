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
    c.execute('''create table if not exists movie(
        no int NOT NULL,
        grade int,
        title varchar(255),
        content varchar(300),
        writer varchar(30),
        date varchar(255)
        )''')
    conn.commit()
    conn.close()

#데이터 입력 함수
def insert_movie(items):
    conn=conn_db()
    c=conn.cursor()
    #데이터 입력방법1
    # c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    #데이터 입력방법2
    sql='insert into movie values(%s,%s,%s,%s,%s,%s)'
    c.executemany(sql, items) 
    #데이터 입력방법3
    # items=[('빅데이터','2014-07-02','삼성',296,11),
    # ('안드로이드','2010-02-02','삼성',526,20),
    # ('spring','2013-12-02','삼성',248,15)]
    # c.executemany(sql,items)
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_movies():
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM movie")
    items=c.fetchall()
    print(type(items))
    print(len(items))
    print(items)

    for item in items:
        for i in item:
            print(item[i], end=" ")
        print()
    
    conn.close()