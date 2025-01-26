class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        visited = [0] * n
        in_cycle = [False] * n
        max_length = 0

        def dfs(node, path):
            if visited[node]:
                return len(path) - path.index(visited[node])
            visited[node] = node
            path.append(node)
            length = dfs(favorite[node], path)
            in_cycle[node] = True
            path.pop()
            return length

        for i in range(n):
            if not visited[i]:
                max_length = max(max_length, dfs(i, []))

        def chain_length(node):
            length = 0
            while favorite[node] != -1:
                length += 1
                temp_node = node
                node = favorite[node]
                favorite[temp_node] = -1
            return length

        result = max_length
        count_two_cycles = 0

        for i in range(n):
            if in_cycle[i]:
                j = favorite[i]
                if favorite[j] == i and not in_cycle[j]:
                    count_two_cycles += chain_length(i) + chain_length(j)

        return max(result, count_two_cycles)