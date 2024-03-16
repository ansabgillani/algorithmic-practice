class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_index = {0: -1}
        max_length = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            # Increment current sum by 1 if num is 1, otherwise decrement by 1
            current_sum += (2 * num) - 1
            
            if current_sum in prefix_sum_index:
                # Calculate the length of the subarray from the first occurrence to the current index
                max_length = max(max_length, i - prefix_sum_index[current_sum])
            else:
                # Store the first occurrence of this prefix sum
                prefix_sum_index[current_sum] = i
        
        return max_length

# Example usage:
# solution = Solution()
# print(solution.findMaxLength([0, 1]))  # Output: 2
# print(solution.findMaxLength([0, 1, 0]))  # Output: 2
# print(solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))  # Output: 6