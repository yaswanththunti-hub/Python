str="programming"
res={}
for i in str:
    if i in res:
        res[i] +=1
    else:
        res[i]=1
for character,count in res.items():
    print(character,"=",count)
