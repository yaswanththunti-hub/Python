class Solution: 
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
s1=Solution()
arr=[1,2,3,4,5,6]
target=7
print(s1.twoSum(arr,target))
