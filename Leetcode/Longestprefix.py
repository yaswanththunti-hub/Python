class Solution:
    def longestCommonPrefix(self,strs):
        result = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return result
                if strs[0][i] != strs[j][i]:
                    return result
            result = result + strs[0][i]
        return result
sol=Solution()
arr=["flower","floor","fly"]
print(sol.longestCommonPrefix(arr))
