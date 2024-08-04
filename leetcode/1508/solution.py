class Solution:
    def rangeSum(self, nums, n, left, right):
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        subarray_sums = []
        for i in range(1, n + 1):
            for j in range(i):
                subarray_sums.append(prefix_sum[i] - prefix_sum[j])
        
        subarray_sums.sort()
        
        result = sum(subarray_sums[left - 1:right]) % (10**9 + 7)
        
        return result