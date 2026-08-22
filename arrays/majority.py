class Solution:
    def majority(self,arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1
            if count>n//2:
                return arr[i]
        return flase
sol=Solution()
arr=[1,4,5,9,9,9,9,1]
print(sol.majority(arr))
        
