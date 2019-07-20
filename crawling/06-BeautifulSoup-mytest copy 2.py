import urllib.request
from bs4 import BeautifulSoup

url='https://music.bugs.co.kr/chart'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
results=soup.select("p.title a")

for result in results:
    print(result.string)