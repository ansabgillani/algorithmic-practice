# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            count = 0
            current = prev_group_end.next
            while current and count < k:
                current = current.next
                count += 1
            
            if count == k:
                # Reverse the k nodes
                current = prev_group_end.next
                next_node = None
                for _ in range(k):
                    temp = current.next
                    current.next = next_node
                    next_node = current
                    current = temp
                
                # Connect the reversed group to the previous group and move pointers
                prev_group_end.next.next = current
                temp = prev_group_end.next
                prev_group_end.next = next_node
                prev_group_end = temp
            else:
                break
        
        return dummy.next