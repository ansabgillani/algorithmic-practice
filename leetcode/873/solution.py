class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Finds the length of the longest Fibonacci-like subsequence in a strictly increasing array.
        
        Args:
            arr (List[int]): The input array of positive integers.
            
        Returns:
            int: The length of the longest Fibonacci-like subsequence. If one does not exist, returns 0.
        """
        n = len(arr)
        idx_map = {num: i for i, num in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        
        max_len = 0
        
        for k in range(2, n):
            for j in range(k-1, 0, -1):
                x = arr[k] - arr[j]
                if x >= arr[j]:
                    break
                i = idx_map.get(x, -1)
                if i < 0:
                    continue
                dp[i][j] = dp[j][k] = max(dp[i][j], dp[j][k]) + 1
                max_len = max(max_len, dp[i][j])
        
        return max_len if max_len > 2 else 0

# Example usage:
# solution = Solution()
# print(solution.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))  # Output: 5
# print(solution.lenLongestFibSubseq([1,3,7,11,12,14,18]))  # Output: 3