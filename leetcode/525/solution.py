class Solution:
    def findMaxLength(self, nums):
        count, max_length = 0, 0
        index_map = {0: -1} # Initial mapping for when the count is zero

        for i, num in enumerate(nums):
            # Increment count for 1, decrement for 0
            count += (2 * num) - 1
            
            if count in index_map:
                max_length = max(max_length, i - index_map[count])
            else:
                index_map[count] = i

        return max_length