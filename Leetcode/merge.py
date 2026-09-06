class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
s=Solution()
list1=[2,3,4]
list2=[5,6,7,8]
print(list1,list2)
