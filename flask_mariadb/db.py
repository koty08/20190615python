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
    c.execute('''create table if not exists users(
    userid varchar(11) NOT NULL,
    email varchar(255) NOT NULL,
    address varchar(255),
    password varchar(255) NOT NULL,
    PRIMARY KEY (userid)
    )''')
    conn.commit()
    conn.close()

#데이터 입력 함수
def insert_users(user):
    conn=conn_db()
    c=conn.cursor()
    #데이터 입력방법1
    # c.execute("insert into users values('Java','2019-05-20','길벗',500,10)")
    #데이터 입력방법2
    sql='insert into users values(%s,%s,%s,%s)'
    c.execute(sql,user)
    #데이터 입력방법3
    # items=[('빅데이터','2014-07-02','삼성',296,11),
    # ('안드로이드','2010-02-02','삼성',526,20),
    # ('spring','2013-12-02','삼성',248,15)]
    # c.executemany(sql,items)
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_users():
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM users")

    users=c.fetchall()
    conn.close()
    return users

def one_user(userid):
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM users WHERE userid= %s", userid)
    user =c.fetchone()
    conn.close()
    return user

#개수 정해서 출력
def some_users(num):
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchmany(num)

    for user in users:
        for i in user:
            print(user[i], end=" ")
        print()
    
    conn.close()

#데이터 수정
def update_users(userid, userv):
    conn=conn_db()
    c= conn.cursor()
    sql = "UPDATE users SET email=%s, address=%s, password=%s WHERE userid =%s"   
    userv.append(userid)
    c.execute(sql, userv)
    conn.commit()
    print('수정 완료!')
    conn.close()

#데이터 삭제
def delete_users(userid):
    conn=conn_db()
    c=conn.cursor()
    sql ="DELETE FROM users WHERE userid = %s"
    c.execute(sql, userid)
    conn.commit()
    print('삭제 완료!')
    conn.close()