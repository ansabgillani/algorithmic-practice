class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        total_split = 0

        def dfs(node: int, parent: int) -> Tuple[int, int]:
            nonlocal total_split
            component_value = values[node]
            count = 0

            for child in graph[node]:
                if child != parent:
                    child_value, child_count = dfs(child, node)
                    if child_value % k == 0:
                        total_split += 1
                    else:
                        component_value += child_value
                        count += child_count

            if component_value % k == 0:
                total_split += 1
            else:
                count += 1

            return component_value, count

        dfs(0, -1)
        return total_split