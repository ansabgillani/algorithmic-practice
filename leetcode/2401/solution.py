class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum length and the current bitmask
        max_length = 0
        current_mask = 0
        left = 0

        # Iterate over each number in the array
        for right in range(len(nums)):
            # Shrink the window from the left if adding nums[right] would violate the nice subarray condition
            while (current_mask & nums[right]) != 0:
                current_mask ^= nums[left]
                left += 1

            # Add nums[right] to the current bitmask
            current_mask |= nums[right]

            # Update the maximum length of the nice subarray found so far
            max_length = max(max_length, right - left + 1)

        return max_length