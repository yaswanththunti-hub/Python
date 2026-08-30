class Solution:
    def removeDuplicates(self, nums):
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


sol = Solution()

nums = [1, 1, 2]

k = sol.removeDuplicates(nums)

print("k =", k)
print("nums =", nums[:k])
