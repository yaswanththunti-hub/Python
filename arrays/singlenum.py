class Solution:
    def single(self,arr):
        result=0
        for i in arr:
            result=result^i
        return result
sol=Solution()
arr=[1,4,4,2,1]
print(sol.single(arr))
