'''for i in range(1,11):
    data = "%d번쨰 줄입니다. \n" % i
    f.write(data)
'''
import random
import time

f=open("./python_basic/word.txt",'r')

lis = [ 'abc', 'def', 'cdq', 'dqwd','fgs','fkoewq','qwpoer','pvbksd','slkadvj']
a= 0

while True:
    print('1.문제불러오기 \n2.타자게임 \n3. 종료')
    ins = int(input('입력 : '))
    if ins == 1:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for line in lines:
            lis.append(line)
        q = random.sample(lis,5)
        print(q)
    elif ins == 2:
        q = random.sample(lis,5)
    elif ins ==3 : break
    input('엔터를 누르면 시작합니다.')
    start = time.time()
    while a<5:
        print('문제 {} : {}\n'.format(a+1, q[a]))
        me = input()
        if me == q[a]:
            print('정답!')
            a+=1
    end = time.time()
    res= end-start
    print('걸린 시간 : %.2f초'% res)

f.close()