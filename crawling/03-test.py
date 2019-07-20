import urllib.parse
import urllib.request

#http://www.dt.co.kr/contents.html?article_no=2019072002109919807010
api='http://www.dt.co.kr/contents.html'
value={
    'article_no' : '2019072002109919807010'
}

params = urllib.parse.urlencode(value)
url = api+'?'+params
data = urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)