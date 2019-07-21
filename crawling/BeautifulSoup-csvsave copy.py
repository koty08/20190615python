import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://lol.inven.co.kr/dataninfo/match/playerList.php')
soup=BeautifulSoup(html, 'html.parser')

table = soup.find_all('table', {'id': 'lolMatchTable'})[0]#인덱스값. 첫번째거
rows = table.find_all('tr')

csvFile=open('crawling/matchhistory.csv', 'wt', newline='',encoding='utf-8')
#csv 파일저장 객체
write=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.find_all(['td', 'th']):
            if cell.get_text() == '소환주문' or cell.get_text() == ' ':
                continue
            csvRow.append(cell.get_text())
        csvRow.pop(len(csvRow)-1)
        write.writerow(csvRow)
finally:
    print('csv로 저장됨')
    csvFile.close()