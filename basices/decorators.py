def main():
    str=input("Enter a string :")
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        res=ptr()
        ans=res.lower()
        print(ans)
        print("leaving inner")
    return inner
ref=outer(main)
ref()
