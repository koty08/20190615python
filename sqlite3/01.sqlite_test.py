import sqlite3

print(sqlite3.version)

conn = sqlite3.connect('sqlite3/example.db')
c= conn.cursor()

c.execute('''
    create table if not exists stocks(
    date text,
    trans text,
    symbol text,
    qty real,
    price real)
    ''')

c.execute('''
            insert into stocks(date,trans,symbol,qty,price)
            values('2006-01-05','BUY','aaa',100,35.14)
    ''')

purchases = [('2006-03-28','BUY','IBM',1000,45.00),
('2006-04-05','BUY','MSFT',1000,72.00),
('2006-04-06','SELL', 'IBM',500,53.00)]
c.executemany('insert into stocks values(?,?,?,?,?)',purchases)
conn.commit()
conn.close()