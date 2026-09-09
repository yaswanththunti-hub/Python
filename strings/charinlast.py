str=input("enter a string :")
str1=""
str2=""
result=""
for i in str:
    if i=="a":
        str1=str1+i
    else:
        str2=str2+i
    result=str2+str1
print(result)
