class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        Checks if there exists a continuous subarray whose sum is multiple of k.
        
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Initialize prefix sum and the corresponding index in a dictionary
        prefix_sum = 0
        indices = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
        
        # Check if the current prefix sum or its difference with k exists in the dictionary
        if prefix_sum not in indices:
            indices[prefix_sum] = i
        else:
            # Ensure subarray length is at least two
            if (i - indices[prefix_sum]) > 1:
                return True
    
        return False