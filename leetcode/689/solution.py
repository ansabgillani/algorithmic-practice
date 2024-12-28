class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        sums = [window_sum]
        
        for i in range(k, n):
            window_sum += nums[i] - nums[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
            sums.append(max_sum)
            
        left = [0]*n
        right = [n-k]*n
        best = 0
        
        for i in range(k, n):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
            
        best = n - k

        for i in range(n-k-1, -1, -1):
            if sums[i+k] >= sums[best]:
                best = i
            right[i] = best

        ans = []
        max_sum = 0
        
        for j in range(k, n-k):
            i, l = left[j-k], right[j+k]
            if sums[i] + sums[j] + sums[l] > max_sum:
                ans = [i, j, l]
                max_sum = sums[i] + sums[j] + sums[l]

        return ans