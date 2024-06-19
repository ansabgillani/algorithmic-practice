class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Helper function to check if we can make at least 'm' bouquets with 'k' flowers each within 'days'
        def canMakeBouquets(days):
            count = 0
            consecutive = 0
            for day in bloomDay:
                if day <= days:
                    consecutive += 1
                    if consecutive == k:
                        count += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return count >= m
        
        n = len(bloomDay)
        if n < m * k:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Example usage:
solution = Solution()
print(solution.minDays([1,10,3,10,2], 3, 1))  # Output: 3
print(solution.minDays([1,10,3,10,2], 3, 2))  # Output: -1
print(solution.minDays([7,7,7,7,12,7,7], 2, 3))  # Output: 12