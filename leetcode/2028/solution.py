from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the sum of the known rolls and the total required sum to achieve the given mean
        current_sum = sum(rolls)
        total_required_sum = mean * (len(rolls) + n)
        remaining_sum = total_required_sum - current_sum
        
        # Check if it's possible to distribute the remaining sum among n dice with values between 1 and 6
        if not (n <= remaining_sum <= 6 * n):
            return []
        
        # Base value for each die in the missing rolls
        base_value = remaining_sum // n
        # Number of dice that need an extra point to reach the exact remaining sum
        extra_points_needed = remaining_sum % n
        
        # Create the result array with base values
        result = [base_value] * n
        # Add one to the first few elements to distribute the extra points
        for i in range(extra_points_needed):
            result[i] += 1
        
        return result