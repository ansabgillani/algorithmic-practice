class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1
        champion_candidates = [i for i in range(n) if in_degree[i] == 0]
        return champion_candidates[0] if len(champion_candidates) == 1 else -1