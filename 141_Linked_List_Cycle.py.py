# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = head
        y = head
        if (head == None) or (head.next == None):
            return False
        while (y) != None and (y.next) != None and (y.next.next) != None:
            x = x.next
            y = y.next.next
            if x == y:
                return True
        return False