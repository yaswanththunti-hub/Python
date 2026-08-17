class Solution:
    def sumoftwo(self,arr,target):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return "yes"
        return "no"
sol=Solution()
arr=[1,2,3,4,5]
target=710
print(sol.sumoftwo(arr,target))
