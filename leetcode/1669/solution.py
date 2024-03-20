class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = list1
        
        # Find the node before the start index 'a'
        p = dummy
        for _ in range(a):
            p = p.next
        
        # Move to the end of list2
        q = list2
        while q and q.next:
            q = q.next
    
        # Connect the part of list1 before 'a' with the head of list2
        p.next = list2
        
        # Find the node after the end index 'b'
        r = dummy
        for _ in range(b+1):
            r = r.next
    
        # Connect the tail of list2 with the remaining part of list1
        q.next = r
        
        return dummy.next