class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of the linked list and returns its head.
    
    Args:
    head (ListNode): The head of the linked list.
    n (int): The position of the node to remove from the end.
    
    Returns:
    ListNode: The head of the modified linked list.
    """
    # Create a dummy node that points to the head
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers, both starting at the dummy node
    first = second = dummy
    
    # Move the first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until the first pointer reaches the end of the list
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from the end by adjusting the next pointer
    second.next = second.next.next
    
    # Return the modified list starting from the dummy's next
    return dummy.next

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# n = 2
# result_head = removeNthFromEnd(head, n)
# while result_head:
#     print(result_head.val, end=" ")
#     result_head = result_head.next
# # Output: 1 2 3 5