import urllib.request
import time
from bs4 import BeautifulSoup

url='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
results=soup.find_all('a', class_ = 'nclicks(cnt_flashart)')

for result in results:
    print(result.text)
    nurl= result['href']
    nres= urllib.request.urlopen(nurl)
    nsoup= BeautifulSoup(nres, 'html.parser')
    nresults=nsoup.select('div._article_body_contents')
    nresults=[each_line.get_text().strip() for each_line in nresults]

    output =''
    for nresult in nresults:
        if nresult =='':
            continue
        if nresult not in ['/', ]:
            output+=nresult.strip()
    output= output.replace('@yna.co.kr▶확 달라진 연합뉴스 웹을 만나보세요▶네이버 [연합뉴스] 채널 구독   ▶뭐 하고 놀까?', '')
    output= output.replace('// flash 오류를 우회하기 위한 함수 추가', '')
    output= output.replace('function _flash_removeCallback()', '')
    output= output.replace('{}','')
    print(output)
    print()

    time.sleep(3)

