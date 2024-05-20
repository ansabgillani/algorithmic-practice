class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculates the sum of all XOR totals for every subset of nums.
        
        :param nums: List of integers representing the array.
        :return: Sum of all XOR totals for every subset.
        """
        total_sum = 0
        num_count = len(nums)
        
        # Iterate over all possible subsets
        for i in range(1 << num_count):
            subset_xor = 0
            for j in range(num_count):
                # Check if the j-th bit of i is set
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        
        return total_sum