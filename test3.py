
class kvadrat(object):
    def __init__(self, a):
        self.a = a
    def maydan(self):
        return pow(self.a,2)
    def peremetr(self):
        return self.a*4
    
num = kvadrat(4)
print(num.maydan())
print(num.peremetr())

class tortmuyeshlik(kvadrat):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
    def maydan(self):
        return (self.a + self.b)/2
    
    def peremetr(self):
        return self.a + self.b

nums = tortmuyeshlik(4,5)
print(nums.maydan())
print(nums.peremetr())


class ushmuyeshlik(tortmuyeshlik):
    def __init__(self, a,b,c):
        super().__init__(a,b)
        self.c = c
    
    def maydan(self):
        return self.a * self.b / 2
    
    def peremetr(self):
        return self.a + self.b +self.c
number = ushmuyeshlik(4,5,6)
print(number.maydan())
print(number.peremetr())


