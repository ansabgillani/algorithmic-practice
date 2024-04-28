class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [0] * n
        total = 0
        depth_sum = [0] * n

        def dfs(node, parent):
            nonlocal count, total
            count[node] = 1
            depth_sum[node] = 0

            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]
                    depth_sum[node] += depth_sum[neighbor] + count[neighbor]

            depth_sum[node] += parent_depth_sum[node] + (n - count[node])

        parent_depth_sum = [0] * n
        dfs(0, -1)

        ans = [0] * n
        parent_depth_sum[0] = 0

        def second_dfs(node, parent):
            nonlocal ans
            ans[node] = depth_sum[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    next_parent_depth_sum = parent_depth_sum[:]
                    next_parent_depth_sum[neighbor] += (n - count[neighbor]) + count[neighbor]
                    second_dfs(neighbor, node)
                    depth_sum[node] -= (depth_sum[neighbor] + count[neighbor])
                    depth_sum[neighbor] += (parent_depth_sum[node] + (n - count[node]))

        second_dfs(0, -1)
        return ans