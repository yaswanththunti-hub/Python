#Inheritance : It is an machanism which allows us to inherite the properties and behaviour of one class to another class
#There 3 class : only parent,only child,both we can create object for only child class
#example 1:
class Parent:
    def __init__(self):
        self.a=10
class child(Parent):
    def __init__(self):
        Parent.__init__(self) #connect constructor using parent class name(pcn.__init--(self)
        self.b=20
c=child()
print(c.b)
print(c.a)

#example 2:
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=20
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c=30
c=C()
print(c.c)
print(c.b)
print(c.a)

#invoking parent class constructor
class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__() #we can connect with super keyword
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30
c=C()
print(c.c)
print(c.b)
print(c.a)

#examople 3:
#PVM automatically connects the constructor
class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
b1=B()
b1.disp_B()
b1.disp_A()
#with empty methods
class Animal:
    def eat(self):
        print("eat")
    def sleep(self):
        print("sleep")
    def sound(self):
        print("sound")
class dog(Animal):
    pass
class cat(Animal):
    pass
class tiger(Animal):
    pass
d1=dog()
d1.eat()

#1.single-level :single parent class and single child class
class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
b1=B()
b1.disp_B()
b1.disp_A()

#2.multi-level
class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
class C(B):
    def disp_C(self):
        print("Inside C")
c1=C()
c1.disp_C()
c1.disp_B()
c1.disp_A()

#3.hirarchical
class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
class C(A):
    def disp_C(self):
        print("Inside C")
b1=B()
c1=C()
c1.disp_C()
c1.disp_A()
b1.disp_A()
b1.disp_B()

#4. multiple
class A:
    def disp_A(self):
        print("Inside A")
class B:
    def disp_B(self):
        print("Inside B")
class C(A,B):
    def disp_C(self):
        print("Inside C")
c1=C()
c1.disp_C()
c1.disp_B()
c1.disp_A()

#5. hybrid
#combination of any inheritance
#In inhertance we follow MRO rule(method resolution order) 
