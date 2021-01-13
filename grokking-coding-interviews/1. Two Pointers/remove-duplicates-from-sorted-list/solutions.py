# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Removes duplicates from a sorted linked list and returns the head of the modified list.
    
    Parameters:
    head (ListNode): The head of the sorted linked list with possible duplicate values.
    
    Returns:
    ListNode: The head of the sorted linked list with unique values.
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Test cases to verify the correctness of the function
def test_deleteDuplicates():
    # Helper function to create a linked list from a list of values
    def create_list(values):
        dummy = ListNode()
        tail = dummy
        for val in values:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next

    # Helper function to convert a linked list back to a list of values
    def list_to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test case 1: Empty list
    assert list_to_array(deleteDuplicates(create_list([]))) == []

    # Test case 2: List with no duplicates
    assert list_to_array(deleteDuplicates(create_list([1, 2, 3]))) == [1, 2, 3]

    # Test case 3: List with all elements the same
    assert list_to_array(deleteDuplicates(create_list([1, 1, 1, 1]))) == [1]

    # Test case 4: List with some duplicates
    assert list_to_array(deleteDuplicates(create_list([1, 1, 2, 3, 3]))) == [1, 2, 3]

# Run the test cases
test_deleteDuplicates()