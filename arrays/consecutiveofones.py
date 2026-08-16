class Solution:
    def consecutive(self,arr):
        count=0
        max=0
        for i in range(len(arr)):
            if arr[i]==1:
                count=count+1
                if count>max:
                    max=count
            else:
                count=0
        return max
sol=Solution()
arr=[1,0,1,1,1,1]
print(sol.consecutive(arr))
                
