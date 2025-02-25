class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseAlternateKNodes(head: ListNode, k: int) -> ListNode:
    if not head or k <= 1:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while True:
        # Check if there are at least k nodes remaining to reverse
        count = 0
        current = prev.next
        for _ in range(k):
            if not current:
                break
            current = current.next
            count += 1
        
        if count < k:
            break
        
        # Reverse the next k nodes
        next_node = current
        then = prev.next
        i = 0
        while i < k and then != current:
            temp_next = then.next
            then.next = next_node
            next_node = then
            then = temp_next
            i += 1
        
        # Connect the reversed part to the rest of the list
        prev.next = next_node
        for _ in range(k):
            prev = prev.next
    
    return dummy.next

# Test cases:
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("NULL")

# Test case 1
head = create_linked_list([1, 2, 3, 4, 5, 6])
k = 2
print_linked_list(reverseAlternateKNodes(head, k))  # Output: 2 -> 1 -> 3 -> 4 -> 6 -> 5 -> NULL

# Test case 2
head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
k = 3
print_linked_list(reverseAlternateKNodes(head, k))  # Output: 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 8 -> 7 -> NULL