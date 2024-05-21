from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets (the power set) of a given list of unique elements.
        
        Args:
            nums: A list of unique integers.
            
        Returns:
            A list of lists containing all possible subsets.
        """
        # Initialize the result with an empty subset
        result = [[]]
        
        # Iterate through each number in the input list
        for num in nums:
            # Append new subsets by adding the current number to existing subsets
            result += [subset + [num] for subset in result]
            
        return result

# Example usage:
sol = Solution()
print(sol.subsets([1, 2, 3]))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(sol.subsets([0]))        # Output: [[], [0]]