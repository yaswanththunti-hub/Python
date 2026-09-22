def outer():
    print("Inside outer") #nonlocal variable 
    def inner():
        print("Inside inner")#local variables 
    inner()
outer()

#legb
from math import pi
#pi=10
def outer():
    #pi=15
    def inner():
        #pi=20
        print(pi)
    inner()
outer()
