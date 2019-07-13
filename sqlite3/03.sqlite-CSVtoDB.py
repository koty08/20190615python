import csv, sqlite3

input_file = 'sqlite3/input.csv'

conn=sqlite3.connect('sqlite3/suppliers.db')
c=conn.cursor()

file_reader=csv.reader(open(input_file, 'r'),delimiter=',') 
# delimiter = 구분자를 뭘로할건지
header=next(file_reader, None)
print(header)

for row in file_reader:
    data=[]
    for idx in range(len(header)):
        data.append(row[idx])
    c.execute('insert into suppliers values(?,?,?,?,?)',data)

conn.commit()