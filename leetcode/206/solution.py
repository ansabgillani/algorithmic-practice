class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move pointers one position ahead
            current = next_node
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: end of the list
        
        new_head = self.reverseListRecursive(head.next)  # Recurse to the end of the list
        head.next.next = head                             # Reverse the link
        head.next = None                                    # Terminate the old list
        return new_head