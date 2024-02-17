import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i - 1
        return n - 1

# Example usage:
sol = Solution()
print(sol.furthestBuilding([4,2,7,6,9,14,12], 5, 1))  # Output: 4
print(sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))  # Output: 7
print(sol.furthestBuilding([14,3,19,3], 17, 0))  # Output: 3