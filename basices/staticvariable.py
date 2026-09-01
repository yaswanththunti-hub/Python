class Farmer:
    r=2.5  #static variable
    def __init__(self,p,t):
        self.principle=p
        self.time=t
    def loan(self):
        si=(self.principle*self.time*Farmer.r)/100
        print(si)
f1=Farmer(200000,3)
f2=Farmer(300000,4)
f2.loan()
f1.loan()
