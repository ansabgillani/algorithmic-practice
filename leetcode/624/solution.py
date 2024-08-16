from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """
        Finds the maximum distance between two integers picked from two different sorted arrays.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables to store the minimum and maximum values found so far
        min_val = float('inf')
        max_val = float('-inf')
        
        # Variable to store the result (maximum distance)
        result = 0
        
        for arr in arrays:
            # Calculate the potential maximum distance using the current array's first element and the global maximum
            result = max(result, arr[-1] - min_val)
            
            # Calculate the potential maximum distance using the current array's last element and the global minimum
            result = max(result, max_val - arr[0])
            
            # Update the global minimum and maximum values
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        
        return result

# Example usage:
# sol = Solution()
# print(sol.maxDistance([[1,2,3],[4,5],[1,2,3]]))  # Output: 4
# print(sol.maxDistance([[1],[1]]))  # Output: 0