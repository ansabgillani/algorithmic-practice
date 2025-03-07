# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the list
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next
        
        # Make the list circular
        k %= length
        if k == 0:
            return head
        
        # Find the new tail and break the list
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        
        # Connect the old tail to the old head to form a circle
        tail.next = head
        
        return new_head