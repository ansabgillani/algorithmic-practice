# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: ListNode) -> ListNode:
    """
    Merges nodes between zeros in a linked list and returns the head of the modified list.
    
    :param head: Head of the linked list
    :return: Modified linked list with merged nodes between zeros
    """
    dummy_head = ListNode(0)
    current = dummy_head
    zero_found = False
    
    while head:
        if head.val == 0:
            zero_found = True
            head = head.next
        else:
            if zero_found:
                current.next = ListNode(head.val)
                current = current.next
                zero_found = False
            head = head.next
    
    return dummy_head.next

# Test cases
def create_linked_list(nums):
    dummy_head = ListNode(0)
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example 1
head1 = create_linked_list([0,3,1,0,4,5,2,0])
result1 = mergeNodes(head1)
print(linked_list_to_list(result1))  # Output: [4, 11]

# Example 2
head2 = create_linked_list([0,1,0,3,0,2,2,0])
result2 = mergeNodes(head2)
print(linked_list_to_list(result2))  # Output: [1, 3, 4]