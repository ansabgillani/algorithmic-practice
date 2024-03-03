class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first, second = first.next, second.next
        
        second.next = second.next.next
        
        return dummy.next