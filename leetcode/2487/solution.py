class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head: ListNode) -> ListNode:
    # Reverse the linked list to process from right to left
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Traverse the reversed list and remove nodes with smaller value than their right neighbor
    dummy_head = ListNode(0)
    dummy_head.next = prev
    max_value = dummy_head.val
    while prev:
        if prev.val < max_value:
            prev = prev.next
        else:
            max_value = prev.val
            prev = prev.next
    
    # Reverse the list back to original order
    result_prev = None
    current = dummy_head.next
    while current:
        next_node = current.next
        current.next = result_prev
        result_prev = current
        current = next_node
    
    return result_prev