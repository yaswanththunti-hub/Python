class Solution:
    def isPalindrome(self, x: int):
        x=str(x)
        return x==x[::-1]
sol=Solution()
x=121
print(sol.isPalindrome(x))
