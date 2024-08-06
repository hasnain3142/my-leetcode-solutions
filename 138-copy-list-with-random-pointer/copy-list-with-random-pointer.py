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
        original_to_copy = {}
        curr = head
        
        while curr:
            original_to_copy[curr] = Node(curr.val)
            curr = curr.next
 
        curr = head
        while curr:
            copy = original_to_copy[curr]
            copy.next = original_to_copy.get(curr.next, None)
            copy.random = original_to_copy.get(curr.random, None)
            curr = curr.next
        
        return original_to_copy.get(head, None)