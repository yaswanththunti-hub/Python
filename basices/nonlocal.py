def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=100
        b=200
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
outer()
