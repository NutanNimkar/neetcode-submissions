# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #use a dummy node when the head is modifying
        dummy = ListNode(0,0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth = self.kthNode(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            start = group_prev.next
            self.reverseLinkedList(start, group_next)
            group_prev.next = kth
            start.next = group_next

            group_prev = start


        return dummy.next
                
    def reverseLinkedList(self, head, kth):
        prev = None
        cur = head
        while cur != kth:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

    def kthNode(self, head, k):
        cur = head
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
            
            