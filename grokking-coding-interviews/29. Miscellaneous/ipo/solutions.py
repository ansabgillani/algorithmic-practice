from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine capital and profit into pairs and sort by capital
        projects = sorted(zip(capital, profits))
        
        # Max-heap to store profits of projects we can afford
        max_heap = []
        i = 0
        
        for _ in range(k):
            # Add all affordable projects to the heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If there are no affordable projects, break early
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            w -= heapq.heappop(max_heap)
        
        return w

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # Output: 4
    print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6