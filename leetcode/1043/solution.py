class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Solves the problem of partitioning an array into subarrays of length at most k,
        and changing their values to become the maximum value of that subarray, to maximize the sum.
        
        Args:
        arr (List[int]): The input integer array.
        k (int): The maximum length of each subarray.
        
        Returns:
        int: The largest sum after partitioning the array.
        """
        n = len(arr)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_max = 0
            for j in range(1, min(k, i) + 1):
                current_max = max(current_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + current_max * j)
        
        return dp[n]