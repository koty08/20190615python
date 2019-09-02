import urllib.request
import pymysql
import db
from bs4 import BeautifulSoup

url = 'https://music.naver.com/listen/top100.nhn?domain=TOTAL_V2'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
table = soup.select_one('table')
table2 = table.select('tr._tracklist_move ')
list_music = []
lyricLocation_list = []
getinfo_list = []

for i,r in enumerate(table2):
    if i==0:
        continue
    else:        
        for j,c in enumerate(r.find_all('td')):
            if j==1:
                rank = int(c.text.strip())
            elif j==3:
                link = c.select_one('img')['src']
                name = c.select_one('a>span.ellipsis').text.strip()
                getinfo_list.append(c.select_one('a')['href'][-7:])
            elif j==4:
                artist=c.text.strip()
            elif j==6:
                loca = c.find('a', class_ = '_lyric')
                lyricLocation_list.append(loca['class'][-1][-8:])
        try:
            music_t = tuple([rank, link, name, artist])
            list_music.append(music_t)
        except:
            pass
# print(lyricLocation_list)
# print(list_music)

# db.create_table()
# db.insert_music(list_music)