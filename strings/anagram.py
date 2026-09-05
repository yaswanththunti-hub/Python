str1="listen"
str2="netsil"
if len(str1)!=len(str2):
    print("not anagram")
else:
    for i in str1:
        count=0
        result=0
        for j in str1:
            if i==j:
                count+=1
        for j in str2:
            if i==j:
                result+=1
    if count!=result:
            print("not anagram")
    else:
            print("anagram")
