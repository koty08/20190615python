import sqlite3

#테이블 생성함수
def create_table():
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer)''')
    conn.commit()
    conn.close()

# create_table()

#데이터 입력 함수

def insert_books(item):
    conn=sqlite3.connect("flask/static/my_books.db")
    c=conn.cursor()
    #입력방법 1
    # c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    #입력방법 2
    sql = 'insert into books values(?,?,?,?,?)'
    c.execute(sql,item)
    # 입력방법 3
    # c.executemany(sql,items)
    conn.commit()
    conn.close()

# insert_books()

#전체 데이터 출력 함수
def all_books():
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute("select * from books")
    print('[1]전체 데이터 출력하기')
    books=c.fetchall()
    print(type(books))
    print(len(books))

    for book in books:
        for i in book:
            print(i, end=" ")
        print()

    conn.close()

# all_books()

#개수 정해서 출력
def some_books(number):
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute("select * from books")
    books=c.fetchmany(number)

    for book in books:
        for i in book:
            print(i, end=" ")
        print()

    conn.close()

# some_books(3)

#한개 출력
def one_book():
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute("select * from books")
    book=c.fetchone()
    print(type(book))
    print(book)
    conn.close()

# one_book()

#조건 지정 및 정렬 검색
def big_books():
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute("select title,pages from books where pages>300 order by pages desc") #desc = 오름차순 정렬
    books=c.fetchall()

    for book in books:
        for i in book:
            print(i, end=" ")
        print()

    conn.close()

# big_books()

def delete_all():
    conn=sqlite3.connect('flask/static/my_books.db')
    c=conn.cursor()
    c.execute('delete from books')
    conn.close()

# delete_all()