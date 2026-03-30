"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashm = {None : None}

        if not head:
            return None
        
        cur = head
        while cur:
            copyNode = Node(cur.val)
            hashm[cur] = copyNode
            cur = cur.next
        cur = head
        while cur:
            copyNode = hashm[cur]
            copyNode.next = hashm[cur.next]
            copyNode.random = hashm[cur.random]
            cur = cur.next
            
        return hashm[head]