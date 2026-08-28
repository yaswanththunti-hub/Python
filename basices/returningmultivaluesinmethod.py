class Calci:
    def __init__(self):
        self.brand="Calsi"
        self.cost=1500
    def cal(self,a,b):
        add=a+b
        sub=a-b
        mul=a*b
        div=a/b
        return add,sub,mul,div
c=Calci()
print(c.brand)
print(c.cost)
x=5
y=2
r1,r2,r3,r4=c.cal(x,y)
print("add of two:",r1)
print("sub of two:",r2)
print("mul of two:",r3)
print("div of two:",r4)
