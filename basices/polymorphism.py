class Animal:
    def Sound(self):
        print("Animal make sound")
class Dog(Animal):
    def Sound(self):
        super().Sound()
        print("Dog barks")
d=Dog()
d.Sound()

class vehicle:
    def Sound(self):
        print("vehicle make sound")
class bike(vehicle):
    def starts(self):
        super().Sound()
        print("bike starts")
d=bike()
d.starts()