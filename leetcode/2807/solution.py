class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head
        current_node = head.next
        
        while current_node:
            gcd_value = self.gcd(prev_node.val, current_node.val)
            gcd_node = ListNode(gcd_value, current_node)
            
            prev_node.next = gcd_node
            
            prev_node = current_node
            current_node = current_node.next
        
        return head

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a