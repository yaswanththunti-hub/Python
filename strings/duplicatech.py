str="programming"
res=""
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
    if count>1 and i not in res:
        res+=i
        print(i)
