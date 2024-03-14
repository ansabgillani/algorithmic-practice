from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Returns the number of non-empty subarrays with a sum equal to the given goal.
        
        :param nums: List of binary numbers.
        :param goal: Target sum for subarrays.
        :return: Number of subarrays with sum equal to goal.
        """
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        current_sum, count = 0, 0
        
        for num in nums:
            current_sum += num
            if (current_sum - goal) in prefix_sum_count:
                count += prefix_sum_count[current_sum - goal]
            prefix_sum_count[current_sum] += 1
        
        return count

# Example usage:
solution = Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1], 2))  # Output: 4
print(solution.numSubarraysWithSum([0,0,0,0,0], 0))  # Output: 15