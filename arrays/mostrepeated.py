class Solution:
    def morerepeated(self,arr):
        maxcount = 0
        mostrepeated = arr[0]
        for i in range(len(arr)):
            count = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count += 1
            if count > maxcount:
                maxcount = count
                mostrepeated = arr[i]
        return mostrepeated
sol=Solution()
arr=[1,2,3,1,1,2,3]
print(sol.morerepeated(arr))
