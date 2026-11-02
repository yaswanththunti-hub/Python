a=int(input("Enter a number :"))
b=int(input("Enter a number :"))

try:
    res=a/b
    print(res)
except Exception as e:
    print("Error occurred")

def fun1():
    print("entering fun1")
    try:q
        fun2()
    except Exception as e:
        print("error occurred in fun1")
    print("leaving fun1")
def fun2():
    print("enterting fun2")
    res =10/0
    print(res)
    print("leaving fun2")
print("program started")
fun1()
print("program ended")

def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error occurred in fun1")
    print("leaving fun1")
def fun2():
    print("enterting fun2")
    try:
        res =10/0
        print(res)
    except Exception as e:
        print("error occurred in fun2")
        raise e
    finally:
        print("leaving fun2")
print("program started")
fun1()
print("program ended")

try:
    a=int(input("enter a num :"))
    b=input("enter a num :")
    res=a/b
    print(res)
except ZeroDivisionError as e:
    print("it is ZDE")
except ValueError as e:
    print("It is VE")
except Exception as e:
    print("other error")


try:
    a=int(input("enter a num :"))
    b=int(input("enter a num :"))
    res=a/b
    print(res)
except (ZeroDivisionError,ValueError) as e:
    print("it is ZDE or VE")
except Exception as e:
    print("other error")

try:
    a=int(input("enter a num :"))
    b=input("enter a num :")
    res=a/b
    print(res)
except Exception as e:
    print("error occurred")
    print(e.__str__())
else:
    print("program successfully")
