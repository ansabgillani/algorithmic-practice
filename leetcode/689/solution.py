class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum_k = [0] * (n - k + 1)
        for i in range(n - k + 1):
            sum_k[i] = sum(nums[i:i+k])
        
        dp = [[0] * (k+1) for _ in range(n)]
        indices = [[-1] * (k+1) for _ in range(n)]
        
        for i in range(n):
            for j in range(1, k+1):
                if i < k:
                    dp[i][j] = sum_k[i]
                    indices[i][j] = i
                else:
                    if dp[i-1][j] > dp[i-k][j-1] + sum_k[i]:
                        dp[i][j] = dp[i-1][j]
                        indices[i][j] = indices[i-1][j]
                    else:
                        dp[i][j] = dp[i-k][j-1] + sum_k[i]
                        indices[i][j] = i - k + 1
        
        result = []
        max_sum = dp[-1][-1]
        for j in range(k, 0, -1):
            result.append(indices[max_sum][j])
            max_sum -= sum_k[result[-1]]
        
        return result[::-1]