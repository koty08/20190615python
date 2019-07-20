import urllib.request
from bs4 import BeautifulSoup

url='https://www.naver.com'
req = urllib.request.urlopen(url)
res = req.read()

soup = BeautifulSoup(res, 'html.parser')
keywords=soup.find_all("span", class_='ah_k')
#get_text() ->데이터에서 문자열만 추출

keywords= [each_line.get_text().strip() for each_line in keywords[:20]]
print(keywords)