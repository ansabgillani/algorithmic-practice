class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head.val
        head = head.next
        index = 1
        critical_points = []
        
        while head.next is not None:
            if (head.val > prev and head.val > head.next.val) or (head.val < prev and head.val < head.next.val):
                critical_points.append(index)
            
            prev, head, index = head.val, head.next, index + 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        min_distance = min(critical_points[i] - critical_points[i-1] for i in range(1, len(critical_points)))
        max_distance = critical_points[-1] - critical_points[0]

        return [min_distance, max_distance]