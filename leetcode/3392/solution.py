class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # Initialize a counter to keep track of valid subarrays
        count = 0
        
        # Iterate through the array with a sliding window of size 3
        for i in range(1, len(nums) - 1):
            # Calculate the required condition
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]):
                count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.countSubarrays([1, 2, 1, 4, 1]))  # Output: 1
# print(sol.countSubarrays([1, 1, 1]))       # Output: 0