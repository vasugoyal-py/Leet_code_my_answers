# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        tail = head

        while l1 or l2 or carry != 0:
            if l1:
                dig1 = l1.val
            else:
                dig1 = 0
            if l2:
                dig2 = l2.val
            else:
                dig2 = 0

            total = dig1 + dig2 + carry
            digit = total % 10
            carry = total // 10

            new = ListNode(digit)
            tail.next = new
            tail = tail.next

            if l1:  
                l1 = l1.next
            else:
                l1 = None 
            if l2:
                l2 = l2.next
            else:
                l2 = None 
        head = head.next
        return head