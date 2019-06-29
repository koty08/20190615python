import json

customer = {
    'id' : 152352,
    'name' : '강진수',
    'history' : [
        {'date' : '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
        ]
}

jsonString = json.dumps(customer)
print(jsonString)
print(type(jsonString))

jsonString = json.dumps(customer, indent=4)
print(jsonString)

#json.dumps 파이썬내에서 바로 사용 s(string)의 의미
jsonString = json.dumps(customer)
print(jsonString)

#json.dump 파일로 바로 저장 
with open("./python_basic/test.json", 'wt') as f: #write text(default가 텍스트라 안적어도 무방)
    json.dump(customer, f, indent=4)

#json.loads json문자를 읽어서 파이썬 객체로 변경 s(string)의 의미
customer1 = json.loads(jsonString)
print(customer1)

#json.load json파일을 읽어서 파이썬 객체로 변경

with open("./python_basic/test.json", 'rt') as f:
    customer2= json.load(f)
    print(type(customer2))
    print(customer2)
