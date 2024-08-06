# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        temp = head
        carry = 0
        while l1 and l2:
            res = l1.val + l2.val + carry
            if res > 9:
                carry, value = res//10, res%10
            else:
                carry, value = 0, res
            temp.next = ListNode(value, None)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            res = l1.val + carry
            if res > 9:
                carry, value = res//10, res%10
            else:
                carry, value = 0, res
            temp.next = ListNode(value, None)
            temp = temp.next
            l1 = l1.next
        
        while l2:
            res = l2.val + carry
            if res > 9:
                carry, value = res//10, res%10
            else:
                carry, value = 0, res
            temp.next = ListNode(value, None)
            temp = temp.next
            l2 = l2.next
            
        if carry:
            temp.next = ListNode(carry, None)
            
        return head.next