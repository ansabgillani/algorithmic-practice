class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Dictionary to store the size of each group based on digit sum
        group_sizes = {}
        
        # Helper function to calculate the sum of digits of a number
        def digit_sum(x):
            return sum(int(digit) for digit in str(x))
        
        # Group numbers by their digit sum
        for i in range(1, n + 1):
            ds = digit_sum(i)
            if ds in group_sizes:
                group_sizes[ds] += 1
            else:
                group_sizes[ds] = 1
        
        # Find the maximum size of any group
        max_size = max(group_sizes.values())
        
        # Count how many groups have this maximum size
        largest_groups_count = sum(1 for size in group_sizes.values() if size == max_size)
        
        return largest_groups_count