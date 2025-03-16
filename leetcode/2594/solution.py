from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Binary search to find the minimum time required
        left = 1
        right = max(ranks) * (cars // len(ranks))**2
        
        while left < right:
            mid = (left + right) // 2
            if self.canRepairInTime(ranks, cars, mid):
                right = mid
            else:
                left = mid + 1
        
        return left

    def canRepairInTime(self, ranks: List[int], cars: int, time: int) -> bool:
        # Check if we can repair all cars in 'time' minutes
        total_cars_repaired = 0
        for rank in ranks:
            n = (time // rank)**0.5
            total_cars_repaired += n
        
        return total_cars_repaired >= cars

# Example usage:
sol = Solution()
print(sol.repairCars([4, 2, 3, 1], 10))  # Output: 16
print(sol.repairCars([5, 1, 8], 6))     # Output: 16