class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the list to be in the form L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ….
        Only nodes themselves may be changed.
        """
        if not head or not head.next:
            return

        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        # Reorder the first and second halves
        first, second = head, prev
        while second.next:  # Ensure we stop before the middle node is linked back to itself
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Test cases
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example 1
head1 = create_linked_list([1,2,3,4])
Solution().reorderList(head1)
print_linked_list(head1)  # Output: 1 -> 4 -> 2 -> 3 -> None

# Example 2
head2 = create_linked_list([1,2,3,4,5])
Solution().reorderList(head2)
print_linked_list(head2)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None