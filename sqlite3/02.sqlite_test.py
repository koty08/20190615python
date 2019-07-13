import sqlite3

conn = sqlite3.connect('sqlite3/example.db')
c= conn.cursor()

symbol = 'aaa'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
items = c.fetchall()

for item in items:
    print(item)


t=('RHAT',)
sql='select * from stocks where symbol=?'
c.execute(sql, t)
print(c.fetchall())

for row in c.execute('select * from stocks order by price'):
    print(row)

c.close()