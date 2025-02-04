class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Finds the maximum possible sum of an ascending subarray in nums.
        
        :param nums: List of positive integers
        :return: Maximum sum of an ascending subarray
        """
        max_sum = 0
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        
        return max(max_sum, current_sum)

# Test cases
print(Solution().maxAscendingSum([10,20,30,5,10,50]))  # Output: 65
print(Solution().maxAscendingSum([10,20,30,40,50]))  # Output: 150
print(Solution().maxAscendingSum([12,17,15,13,10,11,12]))  # Output: 33