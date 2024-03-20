class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    # Create a dummy node to handle edge cases easily
    dummy = ListNode(0)
    dummy.next = list1
    
    # Find the node just before the start of the removal segment
    prev_a = dummy
    for _ in range(a):
        prev_a = prev_a.next
    
    # Find the node at the end of the removal segment
    curr_b = prev_a
    for _ in range(b - a + 2):
        curr_b = curr_b.next
    
    # Connect the end of list1 to the head of list2
    prev_a.next = list2
    
    # Traverse to the end of list2
    while list2 and list2.next:
        list2 = list2.next
    
    # Connect the end of list2 to the node after the removal segment in list1
    list2.next = curr_b
    
    return dummy.next

# Test cases
def test_mergeInBetween():
    # Example 1
    l1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
    l2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = mergeInBetween(l1, 3, 4, l2)
    # Expected output: [10, 1, 13, 1000000, 1000001, 1000002, 5]
    
    # Example 2
    l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    l2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
    result = mergeInBetween(l1, 2, 5, l2)
    # Expected output: [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
    
test_mergeInBetween()