
str=input("enter a string :")
print(str)
if str.isalpha():
    print("string contains only alphabets")
elif str.isdigit():
    print("string contains only numbers")
elif str.isalnum():
    print("string contains both")
else:
    print("other characters")
