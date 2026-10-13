#polymorphism
#method names should be same
#an object performs multiple tasks
class Dog:
    def sleep(self):
        print("dog is sleeping")
    def eat(self):
        print("dog is eating")
class run(Dog):
    def doing(self):
        print("dog is running")
class walk(Dog):
    def doing(self):
        print("dog is walking")
r=run()
w=walk()
def Animal(ref):
    ref.sleep()
    ref.eat()
    ref.doing()
Animal(r)
Animal(w)
