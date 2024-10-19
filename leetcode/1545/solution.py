class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Find the k-th bit in the n-th binary string S_n.
        
        Parameters:
        n (int): The index of the string S_n.
        k (int): The position of the bit to be found in S_n.
        
        Returns:
        str: The k-th bit ('0' or '1') in S_n.
        """
        if n == 1:
            return "0"
        
        length = 2**n - 1
        mid = length // 2
        
        if k == mid + 1:
            return "1"
        elif k < mid + 1:
            return self.findKthBit(n - 1, k)
        else:
            return str(1 - int(self.findKthBit(n - 1, length - k)))