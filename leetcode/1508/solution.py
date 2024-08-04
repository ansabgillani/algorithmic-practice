class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []
        
        # Calculate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
                
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Sum the required range
        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result