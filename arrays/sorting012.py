class Solution:
    def sorting012(self,arr):
        l1=[]
        l2=[]
        l3=[]
        for i in arr:
            if i==0:
                l1.append(i)
            elif i==1:
                l2.append(i)
            elif i==2:
                l3.append(i)
            else:
                print("enter correct values")
        return 11+l2+l3
sol=Solution()
arr=[0,1,2,0,1,2]
print(sol.sorting012(arr))
