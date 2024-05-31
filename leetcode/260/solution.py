class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        set_bit = xor & -xor
        
        num1, num2 = 0, 0
        
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]