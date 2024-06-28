class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Create a graph to represent the cities and their connections
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # Calculate the degree of each city (number of connections)
        degrees = [len(graph[i]) for i in range(n)]
        
        # Sort cities by their degree in descending order
        degrees.sort(reverse=True)
        
        # Assign importance based on the sorted degrees
        importance = list(range(1, n + 1))
        max_importance = sum(degrees[i] * importance[i] for i in range(n))
        
        return max_importance

# Test cases to verify the solution
print(Solution().maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # Output: 43
print(Solution().maximumImportance(5, [[0,3],[2,4],[1,3]]))  # Output: 20