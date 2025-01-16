class Solution:
    def xorAllNums(self, nums1, nums2):
        # Helper function to perform bitwise XOR operation on two numbers
        def xor(a, b):
            return a ^ b
        
        # XOR all elements in nums1 if length of nums2 is odd
        xor_nums1 = reduce(xor, nums1) if len(nums2) % 2 else 0
        
        # XOR all elements in nums2 if length of nums1 is odd
        xor_nums2 = reduce(xor, nums2) if len(nums1) % 2 else 0
        
        # Return the bitwise XOR of both results
        return xor_nums1 ^ xor_nums2