'''#1. 주민번호 성별체크

a= input("주민번호 입력 : ")
print(a[7])
if a[7] == '2' or a[7] == '4':
    print('여자')
else :
    print('남자')
'''
'''#2. 구구단 출력

for i in range(2, 10):
    print('--[%d단]--' %i)
    for j in range(1, 10):
        print("{} X {} = {}".format(i,j,i*j))
'''

'''#2(2).구구단 출력2
for i in range(1, 10):
    for j in range(2, 10):
        print("{} X {} = {:2}".format(j,i,i*j), end =' ')
    print('\n')
'''

'''#3. 커피가격
coffee=dict()
for i in range(3):
    cof = input("커피 이름 입력 :")
    pri = int(input("커피 가격 입력 :"))
    coffee[cof]= pri

for k in coffee.keys():
    print('{}  '.format(k))

a= input("선택 : ")

if a in coffee.keys():
    print(coffee.get(a))
else:
    print('그런 메뉴는 없습니다.')'''

'''#4. 덧셈문제 맞추기
import random 

count = 0

for i in range(10):
    a= random.randint(1,50)
    b= random.randint(1,50)
    res = a+b
    print("{} + {} = ".format(a, b))
    me = int(input())
    if res == me:
        print('정답!')
        count+=1
    else:
        print('오답..')

print('{}개 맞음'.format(count))'''

'''#시간 맞추기 게임
import time

input('엔터를 누르고 20초를 셉니다.\n20초 후에 다시 엔터를 누릅니다.')
start = time.time()
input()
end = time.time()
print('실제 시간 : {}'.format(end-start))
print('차이 : {}'.format(20-(end-start)))'''

'''#숫자 맞추기
import random
com = random.randint(1,100)
count =0
while True:
    me = int(input('1~100사이 숫자를 입력하세요 : '))
    if me>com:
        print('더 작은수를 입력하세요')
        count+=1
    elif me<com:
        print('더 큰수를 입력하세요')
        count+=1
    else:
        count+=1
        print("정답입니다. {}번 만에 맞추셨습니다.".format(count))'''

#로또번호생성
import random

for i in range(5):
    lotto=[]
    for j in range(6):
        a= random.randint(1,45)
        lotto.append(a)
    lotto.sort()
    print("로또 : {}".format(lotto))

