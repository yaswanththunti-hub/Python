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
