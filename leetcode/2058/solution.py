# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev, cur, i, critical_points = None, head, 1, []
        
        while cur and cur.next and cur.next.next:
            nxt = cur.next.next
            if (prev.val < cur.val > nxt.val) or (prev.val > cur.val < nxt.val):
                critical_points.append(i)
            prev, cur, i = cur, nxt, i + 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        for j in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[j] - critical_points[j - 1])
        
        max_distance = critical_points[-1] - critical_points[0]
        
        return [min_distance, max_distance]