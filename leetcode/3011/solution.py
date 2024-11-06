class Solution:
    def canBeSorted(self, nums):
        n = len(nums)
        
        # Helper function to count set bits in binary representation of a number
        def count_set_bits(num):
            return bin(num).count('1')
        
        # Group indices by the number of set bits in their binary representation
        groups = {}
        for i in range(n):
            bits = count_set_bits(nums[i])
            if bits not in groups:
                groups[bits] = []
            groups[bits].append(i)
        
        # Sort each group and merge them back to a single sorted array
        sorted_nums = []
        for indices in groups.values():
            subarray = [nums[i] for i in indices]
            subarray.sort()
            sorted_nums.extend(subarray)
        
        # Check if the original array can be sorted by swapping adjacent elements with the same number of set bits
        prev_bit_count = -1
        curr_index = 0
        while curr_index < n:
            bit_count = count_set_bits(sorted_nums[curr_index])
            
            if bit_count != prev_bit_count and curr_index > 0:
                return False
            
            prev_bit_count = bit_count
            curr_index += 1
        
        return True