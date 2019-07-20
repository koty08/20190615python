import urllib.request
from bs4 import BeautifulSoup

url='https://movie.naver.com/movie/point/af/list.nhn?&page=1'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
r1=soup.select("td.point")
r2=soup.select("td.title > a.movie")
r3=soup.select("td.title")
r4=soup.select("td.num > a.author")
r5=soup.select("td.num")

for i in range(10):
    r3l = r3[i].text
    r3l = r3l.replace('신고', '')
    r3l2 = ''
    for j in r3l:
        if j == '':
            continue
        else:
            r3l2+=j
    print("영화제목 : %s, 평점 : %s점, 140자평 : %s, 글쓴이 : %s, 날짜 : %s" %(r2[i].text, r1[i].text, r3l2.strip(), r4[i].text, r5[i].string))
    print('')