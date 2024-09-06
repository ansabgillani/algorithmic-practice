# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, nums: List[int]) -> ListNode:
    # Create a dummy node to handle edge cases easily
    dummy = ListNode(0)
    dummy.next = head
    
    current = dummy
    while current and current.next:
        if current.next.val in nums:
            current.next = current.next.next  # Skip the node with value in nums
        else:
            current = current.next  # Move to the next node
    
    return dummy.next

# Test cases
def test_removeElements():
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    
    # Helper function to convert a linked list to a list of values
    def linked_list_to_values(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    assert linked_list_to_values(removeElements(create_linked_list([1,2,3]), [1,2,3])) == [4, 5]
    assert linked_list_to_values(removeElements(create_linked_list([1,2,1,2,1,2]), [1])) == [2, 2, 2]
    assert linked_list_to_values(removeElements(create_linked_list([1,2,3,4]), [5])) == [1, 2, 3, 4]
    
test_removeElements()