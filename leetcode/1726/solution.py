from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Counts the number of unique tuples (a, b, c, d) such that a * b = c * d.
        
        :param nums: List of distinct positive integers
        :return: Number of valid tuples
        """
        # Dictionary to store product counts and their corresponding tuple combinations
        product_count = defaultdict(int)
        result = 0
        
        # Iterate over all pairs (i, j) with i < j
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                
                # Add the number of tuples found so far for this product
                result += product_count[prod]
                
                # Increment the count of this product
                product_count[prod] += 2
        
        return result

# Example usage:
# solution = Solution()
# print(solution.tupleSameProduct([2,3,4,6]))  # Output: 8
# print(solution.tupleSameProduct([1,2,4,5,10]))  # Output: 16