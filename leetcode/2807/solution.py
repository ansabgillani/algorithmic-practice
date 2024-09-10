class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to compute GCD using Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Initialize pointers
        current = head
        
        # Traverse the list and insert new nodes with GCD values
        while current and current.next:
            next_node = current.next
            gcd_value = gcd(current.val, next_node.val)
            
            # Insert new node between current and next
            current.next = ListNode(gcd_value, current.next)
            
            # Move to the next pair
            current = next_node
        
        return head