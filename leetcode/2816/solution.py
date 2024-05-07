class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleTheNumber(head: ListNode) -> ListNode:
    # Helper function to reverse the linked list
    def reverseList(node: ListNode) -> ListNode:
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    # Reverse the linked list to process from least significant digit
    reversed_head = reverseList(head)
    
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while reversed_head or carry:
        value = (reversed_head.val if reversed_head else 0) * 2 + carry
        carry = value // 10
        current.next = ListNode(value % 10)
        current = current.next
        
        if reversed_head:
            reversed_head = reversed_head.next
    
    # Reverse the list back to its original order
    return reverseList(dummy.next)

# Test cases
def test_doubleTheNumber():
    def linked_list_to_array(head: ListNode) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    # Example 1
    head1 = ListNode(1, ListNode(8, ListNode(9)))
    expected1 = [3, 7, 8]
    assert linked_list_to_array(doubleTheNumber(head1)) == expected1
    
    # Example 2
    head2 = ListNode(9, ListNode(9, ListNode(9)))
    expected2 = [1, 9, 9, 8]
    assert linked_list_to_array(doubleTheNumber(head2)) == expected2
    
test_doubleTheNumber()