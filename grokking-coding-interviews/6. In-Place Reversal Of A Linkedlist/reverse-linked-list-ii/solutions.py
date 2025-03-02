# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    # Edge case: empty list or single node
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move prev to the node just before the start of the sublist
    for _ in range(left - 1):
        prev = prev.next
    
    # Initialize pointers for reversing
    curr = prev.next
    next_node = None
    
    # Reverse the sublist from left to right
    for _ in range(right - left + 1):
        temp_next = curr.next
        curr.next = next_node
        next_node = curr
        curr = temp_next
    
    # Connect the reversed part with the rest of the list
    prev.next.next = curr
    prev.next = next_node
    
    return dummy.next

# Test cases
def test_reverseBetween():
    # Example 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result1 = reverseBetween(head1, 2, 4)
    print("Example 1:", end=" ")
    while result1:
        print(result1.val, end=" -> ")
        result1 = result1.next
    print("None")
    
    # Example 2
    head2 = ListNode(5)
    result2 = reverseBetween(head2, 1, 1)
    print("Example 2:", end=" ")
    while result2:
        print(result2.val, end=" -> ")
        result2 = result2.next
    print("None")

test_reverseBetween()