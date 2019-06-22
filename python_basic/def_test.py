def add(a, b):
    result =  a+b
    print('a=',a,'b=',b)
    return result

def add_many(*args):
    result =0
    for i in args:
        result = result+i
    return result

def print_kwargs(**args):
    print(args)

print_kwargs(a='k',gfa=23)

a=1
def test_1():
    global a
    a+=1

test_1()
print(a)