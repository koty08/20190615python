class Cookie:
    pass

a=Cookie()
b=Cookie()

print(type(a))
print(type(b))

class FourCal:
    fist =0
    second =0

    def __init__(self, first, second):
        self.first =first
        self.second =second

    def setdata(self, first, second):
        self.first =first
        self.second =second

    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


c=FourCal(4,5)
print(c.add())


class SafeFourcal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first /self.second
        
d=SafeFourcal(5,0)
print(d.div())

class M:
    class_V =0

a=M()
b=M()
print(a.class_V)
print(b.class_V)

M.class_V=5
print(a.class_V)
print(b.class_V)
a.class_V=6

print(a.class_V)
print(b.class_V)