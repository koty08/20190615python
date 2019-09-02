import urllib.request
import pymysql
import crawltest as crawl
import db2
from bs4 import BeautifulSoup

list_music2 = []

for i in range(50):
    url = 'https://music.naver.com/album/index.nhn?albumId='
    url = url + crawl.getinfo_list[i]
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.select_one('div.thumb>a>img')
    link = table['src']
    table = soup.select('dl.desc>dd')
    artist = table[0].text.strip('\n')
    genre = table[1].text
    date = table[2].text
    company = table[3].text
    music2_t = tuple([link, artist, genre, date, company])
    list_music2.append(music2_t)

# db2.create_table()
# db2.insert_music(list_music2)