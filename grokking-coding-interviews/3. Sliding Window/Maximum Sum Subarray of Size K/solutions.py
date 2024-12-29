class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_index = {0: -1}
        max_length = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # Check if there is a subarray (ending at i) which sums to k
            if current_sum - k in prefix_sum_index:
                max_length = max(max_length, i - prefix_sum_index[current_sum - k])
            
            # Store the first occurrence of this prefix sum
            if current_sum not in prefix_sum_index:
                prefix_sum_index[current_sum] = i
        
        return max_length