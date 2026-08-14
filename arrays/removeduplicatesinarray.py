class Solution:
    def removedduplicate(self,arr:list):
        new=[]
        for i in arr:
            if i not in new:
                new.append(i)
        return new
sol=Solution()
arr=[1,3,4,5,6,1,2,3]
print(sol.removedduplicate(arr))
