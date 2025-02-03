class Solution:
    def longestMonotonicSubarray(self, nums):
        max_length = 0
        inc, dec = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1

            max_length = max(max_length, inc, dec)

        return max_length