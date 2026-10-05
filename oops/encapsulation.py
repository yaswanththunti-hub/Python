class Book:
    def __init__(self,page):
        self.__pages=page
b1=Book(100)
print(b1.__pages)


class Book:
    def __init__(self,page):
        self.__pages=page
    def setter(self,val):
        if val>0:
            self.__pages=val
    def getter(self):
        return self.__pages
b1=Book(100)
res=b1.getter()
print(res)
b1.setter(200)
res1=b1.getter()
print(res1)
b1.setter(-99)
res2=b1.getter()
print(res2)

#normal()
class Person:
    def __init__(self):
        self.__names=""
    def setter(self,namee):
        self.__names=namee
    def getter(self):
        return self.__names
p1=Person()
p1.setter("Rahul")
res=p1.getter()
print(res)
p1.setter("Yashu")
res1=p1.getter()
print(res1)

#property function
class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name=val
    getset=property(getter,setter)
p1=Person()
p1.getset="Rahul"
res=p1.getset
print(res)

#@property
class Book:
    def __init__(self):
        self.name=""
    @property
    def display(self):
        return self.__name
    @display.setter
    def display(self,val):
        self.__name=val
p1=Book()
p1.display="Rahul"
res=p1.display
print(res)
