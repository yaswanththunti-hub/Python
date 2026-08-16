class Solution:
    def longestZeroSumSubarray(self, nums):
        prefix = 0
        first = {}
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix == 0:
                ans = i + 1
            elif prefix in first:
                length = i - first[prefix]
                ans = max(ans, length)
            else:
                first[prefix] = i
        return ans
nums = [9, -3, 3, -1, 6, -5]
sol= Solution()
print(sol.longestZeroSumSubarray(nums))
