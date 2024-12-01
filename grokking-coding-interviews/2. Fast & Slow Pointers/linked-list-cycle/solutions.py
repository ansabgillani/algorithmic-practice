class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Determines if there is a cycle in the linked list using Floyd's Tortoise and Hare algorithm.
        
        :param head: The head of the linked list.
        :return: True if there is a cycle in the linked list, otherwise False.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False