class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list to make addition easier
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        dummy_head = ListNode(0)
        carry = 0
        current = dummy_head
        current.next = prev

        # Traverse the reversed list and double each digit while handling carry
        while current:
            total = (current.val * 2) + carry
            current.val = total % 10
            carry = total // 10
            current = current.next
        
        # If there is a carry after the last node, add a new node with carry value
        if carry > 0:
            current = dummy_head
            while current.next:
                current = current.next
            current.next = ListNode(carry)
        
        # Reverse the list again to get the final result in the correct order
        prev = None
        current = dummy_head.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev