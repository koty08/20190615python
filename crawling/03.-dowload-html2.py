import urllib.parse
import urllib.request

#https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%82%AC%ED%83%95
api='https://search.naver.com/search.naver'
values={
    'sm':'top_hty',
    'fbm' : '0',
    'ie': 'utf8',
    'query' : '사탕'
}

params = urllib.parse.urlencode(values)
url = api+'?'+params
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)