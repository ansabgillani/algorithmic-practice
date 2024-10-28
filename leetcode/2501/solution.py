from collections import Counter
from math import isqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Count occurrences of each number
        count = Counter(nums)
        max_length = 0
        
        # Iterate through the numbers to find the longest square streak
        for num in sorted(count):
            if num not in count:
                continue
            length = 1
            while (next_num := num * num) in count:
                count[next_num] -= 1
                if count[next_num] == 0:
                    del count[next_num]
                length += 1
            max_length = max(max_length, length)
        
        return max_length if max_length > 1 else -1

# Example usage:
sol = Solution()
print(sol.longestSquareStreak([4,3,6,16,8,2]))  # Output: 3
print(sol.longestSquareStreak([2,3,5,6,7]))    # Output: -1