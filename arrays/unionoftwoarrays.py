class Solution:
    def union(self,arr1,arr2):
        res=[]
        for i in arr1:
            if i not in res:
                res.append(i)
        for j in arr2:
            if j not in res:
                res.append(j)
        return res
sol=Solution()
arr1=[1,2,3,4]
arr2=[3,4,5,6]
print(sol.union(arr1,arr2))
            
