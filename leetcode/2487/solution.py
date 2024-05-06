# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        stack = []
        current = prev
        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()
            stack.append(current)
            current = current.next
        
        if not stack:
            return None
        
        result_head = stack[0]
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        
        stack[-1].next = None
        return result_head