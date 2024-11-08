class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor_sum = 0
        max_xor_values = [0] * n
        
        for i in range(n-1, -1, -1):
            xor_sum ^= nums[i]
            max_xor_values[i] = xor_sum ^ ((1 << maximumBit) - 1)
        
        return max_xor_values