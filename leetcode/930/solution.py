class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        prefix_sum = 0
        sum_map = {0: 1}  # To handle the case when a subarray starts from index 0

        for num in nums:
            prefix_sum += num
            
            if (prefix_sum - goal) in sum_map:
                count += sum_map[prefix_sum - goal]
        
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = 0
            sum_map[prefix_sum] += 1

        return count