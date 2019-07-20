import urllib.request
from bs4 import BeautifulSoup

url='http://www.cgv.co.kr/movies/'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
results=soup.select("strong.title")

for result in results:
    print(result.string)