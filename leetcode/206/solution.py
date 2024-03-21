# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list iteratively.
        
        :param head: The head of the linked list to be reversed.
        :return: The new head of the reversed linked list.
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move pointers one position ahead
            current = next_node
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list recursively.
        
        :param head: The head of the linked list to be reversed.
        :return: The new head of the reversed linked list.
        """
        if not head or not head.next:
            return head
        
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p