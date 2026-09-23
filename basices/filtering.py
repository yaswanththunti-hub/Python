# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
L=[]
i=0
while i<=4:
    num=int(input("enter a num:"))
    L.insert(i,num)
    i=i+1
print(L)
# i=0
# while i<=4:
#     data=L[i]
#     choice=even(data)
#     if choice==True:
#         print(L[i])
#     i=i+1
# res=list(filter(even,L))
# print(res)
res=list(filter(lambda num:num%2==0,L))
print(res)
