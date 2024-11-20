from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted linked list and return it.

    :param lists: List of k sorted linked lists.
    :return: One sorted linked list.
    """

    if not lists:
        return None

    import heapq
    dummy = ListNode(0)
    current = dummy
    heap = []

    # Push the first node of each list into the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # Move to the next node in the list and push it into the heap
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next