from flask import Flask, render_template, request
import sqlite_copydef as db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data_sqliteinput.html')

@app.route('/dbinsert/', methods = ['POST'])
def dbinsert():
    fff=request.form
    item= tuple(fff.values())
    print(item)
    db.create_table()
    db.insert_books(item)
    return render_template('sqlite_inputcomp.html')
    
if __name__ == '__main__':
    app.run(debug=True)