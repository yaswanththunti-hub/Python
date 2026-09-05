str="i am good boy"
res=0
result=""
str1=str.split()
for i in str1:
    if len(i)>res:
        res=len(i)
        result=i
print(result)
