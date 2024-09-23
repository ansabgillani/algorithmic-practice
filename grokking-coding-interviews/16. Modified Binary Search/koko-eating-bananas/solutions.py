class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours_needed = sum((pile - 1) // mid + 1 for pile in piles)
            
            if hours_needed > h:
                left = mid + 1
            else:
                right = mid
        
        return left