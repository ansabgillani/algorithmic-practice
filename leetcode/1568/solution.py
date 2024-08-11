class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(start):
            visited = set()
            queue = deque([start])
            visited.add(start)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return len(visited)

        def is_one_island():
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        if count > 0: return False
                        count += bfs((i, j))
            return count == 1

        if not is_one_island(): return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_one_island():
                        return 1
                    grid[i][j] = 1

        return 2