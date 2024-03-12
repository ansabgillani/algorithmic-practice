# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: ListNode) -> ListNode:
    """
    Removes consecutive sequences of nodes that sum to zero from the given linked list.
    
    :param head: The head of the linked list.
    :return: The head of the final linked list after removing zero-sum sublists.
    """
    # Dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sums = {0: dummy}
    
    current = head
    
    while current:
        prefix_sum += current.val
        
        if prefix_sum in prefix_sums:
            # Remove nodes between the previous occurrence of this prefix sum and the current node
            to_remove = prefix_sums[prefix_sum].next
            temp_sum = prefix_sum + to_remove.val
            
            while to_remove != current:
                del prefix_sums[temp_sum]
                to_remove = to_remove.next
                temp_sum += to_remove.val
                
            prefix_sums[prefix_sum].next = current.next
        else:
            prefix_sums[prefix_sum] = current
        
        current = current.next
    
    return dummy.next

# Test cases
def test_removeZeroSumSublists():
    def linked_list_to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    def array_to_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head
    
    # Example 1
    head1 = array_to_linked_list([1, 2, -3, 3, 1])
    result1 = removeZeroSumSublists(head1)
    assert linked_list_to_array(result1) == [3, 1], "Test case 1 failed"
    
    # Example 2
    head2 = array_to_linked_list([1, 2, 3, -3, 4])
    result2 = removeZeroSumSublists(head2)
    assert linked_list_to_array(result2) == [1, 2, 4], "Test case 2 failed"
    
    # Example 3
    head3 = array_to_linked_list([1, 2, 3, -3, -2])
    result3 = removeZeroSumSublists(head3)
    assert linked_list_to_array(result3) == [1], "Test case 3 failed"

test_removeZeroSumSublists()