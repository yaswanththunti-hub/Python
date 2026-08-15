class Solution:
    def missingnoinarray(self,arr):
        u=len(arr)+1
        exp=u*(u+1)//2
        act=0
        for i in range(len(arr)):
            act=act+arr[i]
            res=exp-act
        return res
sol=Solution()
arr=[1,2,3,5]
print(sol.missingnoinarray(arr))
