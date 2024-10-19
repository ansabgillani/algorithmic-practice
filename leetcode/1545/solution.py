class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        mid = 2**(n-1)
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        elif k > mid:
            bit = '0' if self.findKthBit(n - 1, 2 * mid - k) == '1' else '1'
            return bit
        else:
            return '1'