class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Determines if a linked list contains a cycle.
        
        Uses Floyd's Tortoise and Hare algorithm to detect a cycle in O(1) space complexity.
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False