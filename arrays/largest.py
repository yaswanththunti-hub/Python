class Solution: #creating a class
    def largest(self,arr:list): #method
        largest=arr[0]
        for num in arr:
            if num>largest:
                largest=num
        return largest
sol=Solution() #creating a object
arr=[2,5,1,5,4,11]
print(sol.largest(arr))
        
