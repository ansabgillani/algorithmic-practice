# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    # Helper function to reverse a linked list
    def reverseList(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the linked list
    second_half_head = reverseList(slow)
    
    # Compare the first half with the reversed second half
    first_half = head
    second_half = second_half_head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    # Restore the original linked list by reversing the second half again (optional)
    reverseList(second_half_head)
    
    return True

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
# print(isPalindrome(head))  # Output: True