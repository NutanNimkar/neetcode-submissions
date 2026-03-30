# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode(0)
        head = mergedList
       
        while list1 and list2:
            if list1.val <= list2.val:
                mergedList.next = list1
                list1 = list1.next

            elif list2.val < list1.val:
                mergedList.next = list2
                list2 = list2.next
            mergedList = mergedList.next

        if not list2:
            mergedList.next = list1
        if not list1:
            mergedList.next = list2

        return head.next
    
