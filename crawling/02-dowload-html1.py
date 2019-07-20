import urllib.request

url= 'http://biz.chosun.com/site/data/html_dir/2019/07/19/2019071902422.html?utm_source=naver&utm_medium=newsstand&utm_campaign=biz'

mem=urllib.request.urlopen(url).read()
print(mem)
print(mem.decode('utf-8'))