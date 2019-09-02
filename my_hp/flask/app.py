from flask import Flask, render_template, request, redirect
import db
import db2
import lyric_crawl as lyr

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/chart')

@app.route('/chart')
def music_chart():
    db.create_table()
    all_musics=db.all_music()
    return render_template('music_chart.html', musics = all_musics)

@app.route('/music_info/<rank>')
def info(rank):
    lyric = lyr.lyric_list[int(rank)-1]
    music=db2.all_music(int(rank)-1)
    return render_template('music_info.html', lyric = lyric, music = music)

if __name__ == '__main__':
    app.run(debug=True)