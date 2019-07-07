from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes/')
def cakes():
    return 'Yummy cakes!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username, age):
    #return 'Username %s, 나이 %d' % (username,age)
    return render_template('index.html', username=username, age=age)

@app.route('/forminput/')
def forminput():
    return render_template('forminput.html')

@app.route('/method/', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "Post"
    else:
        return "Get"

@app.route('/login/')
def login():
    username = request.args.get('name')
    return render_template('index.html', username=username)

@app.route('/forminput1/')
def forminput1():
    return render_template('forminput1.html')

@app.route('/login/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    return render_template('index.html', username=username, password = password)
    
if __name__ == '__main__':
    app.run(debug=True)