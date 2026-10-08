class Parent:
    def __init__(self):
        self.a=10
class child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=20
c=child()
print(c.b)
print(c.a)

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

invoking parent class constructor

class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30
c=C()
print(c.c)
print(c.b)
print(c.a)

class A:
    def disp_A(self):
        print("Inside A")
class B(A):
    def disp_B(self):
        print("Inside B")
b1=B()
b1.disp_B()
b1.disp_A()
