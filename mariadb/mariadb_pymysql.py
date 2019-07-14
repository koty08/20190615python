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
    c.execute('''create table if not exists books(
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommend integer)''')
    conn.commit()
    conn.close()

#데이터 입력 함수
def insert_books():
    conn=conn_db()
    c=conn.cursor()
    #데이터 입력방법1
    # c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    #데이터 입력방법2
    sql='insert into books values(%s,%s,%s,%s,%s)'
    c.execute(sql,('Python','201001','한빛',584,20))
    #데이터 입력방법3
    # items=[('빅데이터','2014-07-02','삼성',296,11),
    # ('안드로이드','2010-02-02','삼성',526,20),
    # ('spring','2013-12-02','삼성',248,15)]
    # c.executemany(sql,items)
    conn.commit()
    conn.close()

#전체 데이터 출력 함수
def all_books():
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM books")

    print('[1]전체 데이터 출력하기')

    books=c.fetchall()
    print(type(books))
    print(len(books))
    print(books)

    for book in books:
        for i in book:
            print(book[i], end=" ")
        print()
    
    conn.close()

#개수 정해서 출력
def some_books(num):
    conn=conn_db()
    c=conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchmany(num)

    for book in books:
        for i in book:
            print(book[i], end=" ")
        print()
    
    conn.close()

#데이터 수정
def update_books():
    conn=conn_db()
    c= conn.cursor()
    sql = "UPDATE books SET recommend = %s WHERE title =%s"   
    c.execute(sql,(200,'Java'))
    conn.commit()
    conn.close()

#데이터 삭제
def delete_books():
    conn=conn_db()
    c=conn.cursor()
    sql="DELETE FROM books WHERE publisher = '한빛'"
    c.execute(sql)
    conn.commit()
    conn.close()