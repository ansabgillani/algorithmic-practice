class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Helper function to determine if we can allocate 'mid' candies to each child
        def canAllocate(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k
        
        # Edge case: If total number of candies is less than k, no child can get any candies
        if sum(candies) < k:
            return 0
        
        # Binary search to find the maximum number of candies each child can get
        left, right = 1, max(candies)
        while left <= right:
            mid = (left + right) // 2
            if canAllocate(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result