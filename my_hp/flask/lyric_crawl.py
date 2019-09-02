import urllib.request
import pymysql
import crawltest as crawl
from bs4 import BeautifulSoup


lyric_list = []

for i in range(50):
    url = 'https://music.naver.com/lyric/index.nhn?trackId='
    url = url + crawl.lyricLocation_list[i]
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.select_one('div#lyricText')
    lyric_list.append(table.text)