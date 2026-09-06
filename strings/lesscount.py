str="python is a programming language"
str1=str.split()
less=len(str1[0])
res=""
for i in str1:
    if len(i)<less:
        less=len(i)
        res=i
print(res)
