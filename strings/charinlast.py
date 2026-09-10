str=input("enter a string :")
str1=""
str2=""
for i in str:
    if i=="a":
        str1=str1+i
    else:
        str2=str2+i
print(str2+str1)

# str=input("enter the string :")
# ans=""
# for i in str:
#     if i!="a":
#         ans=ans+i
# while(len(ans)<len(str)):
#     ans=ans+"a"
# print(ans)
