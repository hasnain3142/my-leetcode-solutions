# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding Middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse 2nd half list
        prev, curr = None, slow.next
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        print(slow.val)
        slow.next = None

        head1, head2 = head, prev
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            
            head1.next = head2
            head1 = next1
            
            head2.next = head1
            head2 = next2
            