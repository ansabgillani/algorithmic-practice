from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if a given capacity is sufficient to ship within the given number of days
        def can_ship(capacity):
            current_load = 0
            days_required = 1
            for weight in weights:
                if weight > capacity:
                    return False
                if current_load + weight <= capacity:
                    current_load += weight
                else:
                    days_required += 1
                    current_load = weight
            return days_required <= days
        
        # Binary search to find the minimum capacity required
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Example usage:
# sol = Solution()
# print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15