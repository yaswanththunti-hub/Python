class Solution:
    def second_largest(self,arr:list):
        largest=arr[0]
        sec_large=arr[0]
        for num in arr:
            if num>largest:
                sec_large=largest
                largest=num
            elif num>sec_large and num!=largest:
                sec_large=largest                
        return sec_large
sol=Solution()
arr=[5,6,9,3]
print(sol.second_largest(arr))

                
