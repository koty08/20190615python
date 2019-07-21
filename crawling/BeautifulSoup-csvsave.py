import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup=BeautifulSoup(html, 'html.parser')

table = soup.find_all('table', {'class': 'wikitable'})[0] #인덱스값. 첫번째거
rows = table.find_all('tr')

csvFile=open('crawling/editors.csv', 'wt', newline='',encoding='utf-8')
#csv 파일저장 객체
write=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.find_all(['td', 'th']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)
finally:
    print('csv로 저장됨')
    csvFile.close()