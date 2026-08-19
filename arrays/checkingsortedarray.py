class Sorting:
    def checks(self,arr:list):
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                    return False
        return True
c=Sorting()
arr=[1,2,3,4,5,6]
print(c.checks(arr))
