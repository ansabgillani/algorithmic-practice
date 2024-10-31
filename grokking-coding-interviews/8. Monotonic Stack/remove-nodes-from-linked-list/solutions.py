class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list to process from right to left
        def reverse_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Reverse the list to make it easier to remove nodes with greater values on the right
        reversed_head = reverse_list(head)
        
        # Initialize pointers for traversal and removal
        current = reversed_head
        max_val_so_far = current.val
        
        # Traverse the list and remove nodes with smaller value than the current maximum
        while current.next:
            if current.next.val < max_val_so_far:
                current.next = current.next.next
            else:
                max_val_so_far = current.next.val
                current = current.next
        
        # Reverse the list back to its original order
        return reverse_list(reversed_head)