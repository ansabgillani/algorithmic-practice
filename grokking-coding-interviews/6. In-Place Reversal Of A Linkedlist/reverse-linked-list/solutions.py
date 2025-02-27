# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list and returns the new head of the reversed list.

    Args:
    head (ListNode): The head of the original linked list.

    Returns:
    ListNode: The head of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move pointers one position ahead
        current = next_node
    return prev