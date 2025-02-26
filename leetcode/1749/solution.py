class Solution:
    def maxAbsoluteSum(self, nums):
        max_sum = min_sum = curr_max_sum = curr_min_sum = 0

        for num in nums:
            curr_max_sum = max(curr_max_sum + num, num)
            curr_min_sum = min(curr_min_sum + num, num)

            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max(max_sum, -min_sum)