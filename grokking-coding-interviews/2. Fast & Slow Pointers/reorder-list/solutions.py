# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the linked list to the form L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → …
    
    :param head: The head of the singly-linked list.
    """
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    
    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        first_next, second_next = first.next, second.next
        first.next = second
        first = first_next
        second.next = first
        second = second_next

# Test cases to verify the solution
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example 1
head1 = create_linked_list([1, 2, 3, 4])
reorderList(head1)
print_list(head1)  # Output: 1 -> 4 -> 2 -> 3 -> None

# Example 2
head2 = create_linked_list([1, 2, 3, 4, 5])
reorderList(head2)
print_list(head2)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None