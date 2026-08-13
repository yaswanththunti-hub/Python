class Solution:
    def sortedarray(self,arr:list):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
s1=Solution()
arr=[1,3,6,7,4]
print(s1.sortedarray(arr))
