from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_admin():
    return render_template('bootstrap.html')

@app.route('/lol')
def lol():
    return render_template('bootstrap2.html')

if __name__ == '__main__':
    app.run(debug=True)