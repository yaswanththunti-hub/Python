def outer():
    print("Inside outer") #nonlocal variable 
    def inner():
        print("Inside inner")#local variables 
    inner()
outer()
