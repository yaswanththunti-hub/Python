#methods
#1.no parameter no return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
c1=Calci()
print(c1.brand)
print(c1.cost)
c1.add()

#2.no parameters with return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self):
        a=10
        b=20
        c=a+b
        return c
c1=Calci()
print(c1.brand)
print(c1.cost)
res=c1.add()
print(res)

#3.parameters with no return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self,a,b):
        c=a+b
        print(c)
c1=Calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
c1.add(x,y)

#4. parameter with return value
class Calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self,a,b):
        c=a+b
        return c
c1=Calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
result=c1.add(x,y)
print(result)

#static
#class
class Mobile:
    def __init__(self):
        self.brand="oneplus"
    def call(self):
        print("mobile is ringing")
    @staticmethod
    def charging():
        print("mobile is charging")\
    @classmethod
    def off(cls):
        print("mobile is off")
m1=Mobile()
print(m1.brand)
m1.call()
Mobile.charging()
Mobile.off()
