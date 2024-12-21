class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        
        # Build the adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            local_sum = values[node]
            count = 0
            
            # Traverse all children
            for neighbor in graph[node]:
                if neighbor != parent:
                    child_sum, child_count = dfs(neighbor, node)
                    if child_sum % k == 0:
                        nonlocal result
                        result += 1
                        local_sum += child_sum
                        count += child_count
            return local_sum, count + 1
        
        result = 0
        dfs(0, -1)  # Start DFS from the root node (node 0)
        
        # If the total sum is divisible by k, we can have an additional component
        if sum(values) % k == 0:
            result += 1
            
        return result

# Example usage:
solution = Solution()
print(solution.maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6))  # Output: 2
print(solution.maxKDivisibleComponents(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3))  # Output: 3