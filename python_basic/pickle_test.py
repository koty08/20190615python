import pickle 

#파일로 저장
f = open("./python_basic/test.pickle", 'wb') #write binary(바이너리 형식이라는 뜻)
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

#파이썬 내에서 바이트 형태로 사용
datab= pickle.dumps(data)
print(type(datab))

#파일 읽어오기
with open("./python_basic/test.pickle", 'rb') as f:
    data = pickle.load(f)
    print(data)

#바이트 타입을 파이썬형태로 변경
data1 = pickle.loads(datab)
print(data1)
print(type(data1))