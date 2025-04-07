class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # If the total sum is odd, it's impossible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # Target sum for each subset
        target = total_sum // 2
        
        # Initialize a set with a single element: 0
        dp = {0}
        
        # Iterate over each number in the array
        for num in nums:
            # Create a new set to store the updated possible sums
            next_dp = set(dp)
            for current in dp:
                if current + num <= target:
                    next_dp.add(current + num)
            dp = next_dp
        
        # Check if the target sum is achievable
        return target in dp