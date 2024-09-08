# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: 'ListNode', k: int) -> List['ListNode']:
        # Helper function to get the length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # Get the total length of the linked list
        n = get_length(head)
        
        # Base size of each part and extra nodes to distribute
        base_size = n // k
        extras = n % k
        
        result = []
        current = head
        
        for i in range(k):
            if not current:
                result.append(None)
                continue
            
            # Determine the size of the current part
            part_size = base_size + (1 if i < extras else 0)
            
            # Split the list and move to the next part
            dummy = ListNode(0)
            dummy.next = current
            for _ in range(part_size - 1):
                if current:
                    current = current.next
            
            # Break the link for the current part
            next_part = None
            if current:
                next_part = current.next
                current.next = None
                
            result.append(dummy.next)
            current = next_part
        
        return result