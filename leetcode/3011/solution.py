class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        Check if the array can be sorted by swapping adjacent elements with the same number of set bits.
        
        Args:
        nums (List[int]): The input list of positive integers.
        
        Returns:
        bool: True if the array can be sorted, otherwise False.
        """
        def count_set_bits(n):
            """Count the number of set bits in an integer."""
            return bin(n).count('1')
        
        # Group numbers by their number of set bits
        groups = {}
        for num in nums:
            bit_count = count_set_bits(num)
            if bit_count not in groups:
                groups[bit_count] = []
            groups[bit_count].append(num)
        
        # Sort each group and merge them back into a single list
        sorted_nums = []
        for bit_count in sorted(groups):
            sorted_groups = sorted(groups[bit_count])
            sorted_nums.extend(sorted_groups)
        
        # Check if the merged list is sorted
        return sorted_nums == sorted(nums)