class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, root, k):
        length = 0
        current = root
        while current:
            length += 1
            current = current.next

        base_size = length // k
        extra_parts = length % k

        result, current = [], root
        for i in range(k):
            head = tail = ListNode(None)
            for j in range(base_size + (1 if i < extra_parts else 0)):
                if current:
                    tail.next = current
                    current = current.next
                    tail = tail.next
            tail.next = None
            result.append(head.next)

        return result