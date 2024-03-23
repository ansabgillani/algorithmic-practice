class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
            
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2