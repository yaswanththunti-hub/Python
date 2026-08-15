class Solution:
    def movezeros(self,arr:list):
        result=[]
        zeros=[]
        for i in arr:
            if i!=0:
                result.append(i)
            elif i==0:
                zeros.append(i)
        return result+zeros
sol=Solution()
arr=[1,3,0,0,2]
print(sol.movezeros(arr))
