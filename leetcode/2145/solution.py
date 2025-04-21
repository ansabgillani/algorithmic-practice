class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Calculate prefix sums to determine the range of the hidden sequence
        prefix_sums = list(accumulate(differences))
        
        # Find the minimum and maximum values in the prefix sums
        min_prefix = min(prefix_sums)
        max_prefix = max(prefix_sums)
        
        # Calculate the total range that the hidden sequence can cover
        total_range = upper - lower
        
        # Calculate the required range for the prefix sums to fit within the given bounds
        required_range = max_prefix - min_prefix
        
        # The number of valid starting points is the difference between the total range and the required range plus one
        num_valid_starting_points = total_range - required_range + 1
        
        # If the required range exceeds the total range, there are no valid sequences
        if num_valid_starting_points < 0:
            return 0
        
        return num_valid_starting_points