class Solution:
    def rotateKelement(self,arr:list,k:int,dir:str):
        n=len(arr)
        for a in range(k):
            if dir=="left":
                temp=arr[0]
                for i in range(len(arr)-1):
                    arr[i]=arr[i+1]
                arr[len(arr)-1]=temp
            elif dir=="right":
                temp=arr[len(arr)-1]
                for i in range(len(arr)-1,0,-1):
                    arr[i]=arr[i-1]
                arr[0]=temp
        return arr
sol=Solution()
arr=[1,2,3,4,5]
dir="right"
k=3
print(sol.rotateKelement(arr,k,dir))
