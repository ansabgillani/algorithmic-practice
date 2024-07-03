class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        Find the minimum difference between the largest and smallest value in at most 3 moves.
        
        :param nums: List of integers
        :return: Minimum difference after performing at most 3 moves
        """
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        # Consider the effect of changing the three largest or three smallest elements
        min_diff = float('inf')
        for i in range(4):
            min_diff = min(min_diff, nums[n-4+i] - nums[i])
        
        return min_diff