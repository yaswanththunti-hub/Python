class Radio:
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.r=Radio()#creating obj of Radio
c1=Car(60,180)
print(c1.cmin)
print(c1.cmax)
c1.r.turnon(1)
c1.r.turnon(2)

class OS:
    def __init__(self):
        self.status=True
        print("OS is ready")
        print("OS is installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("Mobile is Ready")
        print("with OS installed")
    def getOS(self):
        print("Welcome to Linux")
m1=Mobile("Nokia")
print(m1.mname)
m1.getOS()
print(m1.o.status)
del m1
print(m1.o.status)

class charger:
    def __init__(self,name):
        self.cname=name
    def getcharger(self):
        print("charging")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def getmobile(self,p):
        self.c=p
m1=Mobile("mi")
c1=charger("mic")
m1.getmobile(c1)
print(m1.mname)
print(m1.c.cname)
m1.c.getcharger()
del m1
print(c1.cname)
c1.getcharger()


class Heart:
    def __init__(self):
        self.status="Single"
class Car:
    def __init__(self):
        self.cname="Nexon"
    def start(self):
        print("car is started")
class Person:
    def __init__(self):
        self.pname="Tikku"
        self.h=Heart()
        self.c=""
    def hascar(self,p):
        self.c=p
p1=Person()
c1=Car()
p1.hascar(c1)
print(p1.pname)
print(p1.h.status)
print(p1.c.cname)
p1.c.start()
del p1
print(c1.cname)
c1.start()
print(p1.h.status)
