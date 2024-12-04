class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast
        slow = fast = head
        
        # Phase 1: Finding the intersection point of the two runners
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Phase 2: Finding the entrance to the cycle
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                
                return pointer
        
        # If there is no cycle, return None
        return None