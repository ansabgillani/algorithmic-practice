import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        Maximize capital after at most k projects.
        
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Create a list of (capital, profit) pairs and sort by capital
        projects = sorted(zip(capital, profits))
        
        # Max heap to store available projects' profits
        max_heap = []
        i = 0
        
        for _ in range(k):
            # Add all projects that can be started with the current capital to the max heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If there are no available projects, break the loop
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            w -= heapq.heappop(max_heap)
        
        return w

# Example usage:
sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # Output: 4
print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6