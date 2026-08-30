
class Solution:
    def rearrangeArray(self, arr):
        ans = [0] * len(arr)
        pos = 0
        neg = 1
        for num in arr:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        return ans
sol = Solution()
arr=[1,2,-4,-5]

print(sol.rearrangeArray(arr))
