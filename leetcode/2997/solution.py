class Solution:
    def minOperations(self, nums, k):
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        return bin(xor_sum ^ k).count('1')