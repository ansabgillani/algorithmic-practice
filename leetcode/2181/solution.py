class Solution:
    def mergeNodes(self, head):
        dummy_head = current = ListNode(0)
        
        total = 0
        
        while head:
            if head.val == 0 and total != 0:
                current.next = ListNode(total)
                current = current.next
                total = 0
            elif head.val != 0:
                total += head.val
            
            head = head.next
        
        return dummy_head.next