from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/list')

@app.route('/inputform')
def inputform():
    return render_template('mariadb_input.html')
    
@app.route('/dbinsert/', methods=['POST'])
def dbinsert():
    fff=request.form
    item= tuple(fff.values())
    print(item)
    db.create_table()
    db.insert_users(item)
    return redirect('/list')

@app.route('/list/')
def list_user():
    db.create_table()
    users=db.all_users()
    return render_template('list.html',users=users)

@app.route('/contents/<userid>')
def contents(userid):
    user =db.one_user(userid)
    return render_template('contents.html', user = user)

@app.route('/delete/<userid>')
def delete(userid):
    db.delete_users(userid)
    return redirect('/list')

@app.route('/updateinput/<userid>')
def updateinput(userid):
    return render_template('updateinput.html', userid = userid)

@app.route('/update/<userid>', methods = ['POST'])
def update(userid):
    userv = request.form
    userv = list(userv.values())
    db.update_users(userid, userv)
    return redirect('list')

if __name__ == '__main__':
    app.run(debug=True)