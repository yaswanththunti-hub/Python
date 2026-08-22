class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i],current + nums[i])
            if current > maximum:
                maximum = current
        return maximum
sol = Solution()
nums = [-2, -3, -7, -2, -10, -4] 
print(sol.maxSubArray(nums))
