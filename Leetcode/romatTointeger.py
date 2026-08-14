class Solution:
    def romanToInt(self, s: str):
        roman={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        x=0
        for i in range(len(s)):
            if i< len(s)-1 and roman[s[i]]< roman[s[i+1]]:
                x-=roman[s[i]]
            else:
                x+=roman[s[i]]
        return x
r1=Solution()
s="MMIV"
print(r1.romanToInt(s))
