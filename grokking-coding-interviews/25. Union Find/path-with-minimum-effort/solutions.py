class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Finds the minimum effort required to travel from the top-left cell to the bottom-right cell in a 2D array.
        
        Args:
        heights (List[List[int]]): A 2D list representing the height of each cell.

        Returns:
        int: The minimum effort required to travel from the top-left cell to the bottom-right cell.
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(0, 0, 0)]  # (effort, row, col)
        visited = set()

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(heap, (new_effort, nr, nc))