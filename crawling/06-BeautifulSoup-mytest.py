import urllib.request
from bs4 import BeautifulSoup

url='https://music.naver.com/listen/top100.nhn?domain=TOTAL'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
results=soup.select("td.name span.ellipsis")

rank = 1
for result in results:
    print('%d등: '%rank+ result.string.strip())
    rank+=1