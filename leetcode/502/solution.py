class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        max_heap = []
        sorted_projects = sorted(zip(capital, profits))
        i = 0
        n = len(profits)
        for _ in range(k):
            while i < n and sorted_projects[i][0] <= w:
                heapq.heappush(max_heap, -sorted_projects[i][1])
                i += 1
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)

        return w

# Example usage
sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # Output: 4
print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # Output: 6