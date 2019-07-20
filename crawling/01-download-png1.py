import urllib.request
import os

#이미지 주소
url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqkWPPThP0jxDqJId_h5b0RuqtwkiTnFPuBSkTNiDkkckbvICjkA'

#실행하는 파일 경로 찾아서 같은경로 이미지 저장
dirname=os.path.dirname(__file__)
savename=dirname+'/test.png'


'''#파일로 저장
urllib.request.urlretrieve(url,savename)'''

#파일 저장 2
mem= urllib.request.urlopen(url).read() #파일 불러오기

#위에서 불러온 파일 저장
print(savename)
with open(savename, mode='wb')as f:
    f.write(mem)
    print('저장됨')
