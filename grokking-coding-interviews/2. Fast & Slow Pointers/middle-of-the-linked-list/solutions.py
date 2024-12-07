# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast
        slow = fast = head
        
        # Move fast pointer by 2 steps and slow pointer by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow