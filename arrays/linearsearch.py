class Solution:
    def linersearch(self,arr:list,target):
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return "not found"
sol=Solution()
arr=[10,20,30,40]
target=30
print(sol.linersearch(arrtarget))
