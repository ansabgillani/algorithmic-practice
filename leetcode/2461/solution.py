class Solution:
    def maxSumOfDistinctSubarrays(self, nums, k):
        count = {}
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                return 0
        
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            count[nums[i]] = 1
            
            if count[nums[i-k]] > 1:
                window_sum -= nums[i-k]
                count[nums[i-k]] -= 1
            elif count[nums[i-k]] == 1:
                del count[nums[i-k]]
        
            max_sum = max(max_sum, window_sum)

        return max_sum if max_sum > 0 else 0