from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/chart')

@app.route('/chart')
def music_chart():
    db.create_table()
    all_musics=db.all_music()
    return render_template('music_chart.html', musics = all_musics)

if __name__ == '__main__':
    app.run(debug=True)