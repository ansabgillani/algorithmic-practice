class Solution:
    def countSubarrays(self, nums, k):
        max_num = max(nums)
        total_count = 0
        subarray_count = 0
        start_index = 0

        for end_index, num in enumerate(nums):
            if num == max_num:
                subarray_count += 1
            
            while subarray_count >= k:
                total_count += len(nums) - end_index
                if nums[start_index] == max_num:
                    subarray_count -= 1
                start_index += 1

        return total_count