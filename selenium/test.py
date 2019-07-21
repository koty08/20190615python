from bs4 import BeautifulSoup
import requests
#urllib과 같은 동작
starbugs=requests.get('https://www.istarbucks.co.kr/store/store_map.do')
st_bs = BeautifulSoup(starbugs.text, 'lxml')
print(st_bs.select('li.quickResultLstCon'))