class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffixSum = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i+1]
        
        memo = {}
        
        def dfs(i: int, M: int) -> int:
            if i >= n:
                return 0
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            maxStones = float('-inf')
        
            for X in range(1, min(2*M + 1, n - i + 1)):
                stonesTaken = suffixSum[i] - dfs(i + X, max(M, X))
                
                maxStones = max(maxStones, stonesTaken)
        
            memo[(i, M)] = maxStones
            return memo[(i, M)]
    
        return dfs(0, 1)

# Test cases
solution = Solution()
print(solution.stoneGameII([2,7,9,4,4]))  # Output: 10
print(solution.stoneGameII([1,2,3,4,5,100]))  # Output: 104