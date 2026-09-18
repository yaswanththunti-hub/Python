def outer():
    print("Inside outer")
    def inner():
        print("Inside inner")
    inner()
outer()
