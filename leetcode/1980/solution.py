class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        for i in range(2**n):
            bin_str = format(i, f'0{n}b')
            if bin_str not in nums:
                return bin_str