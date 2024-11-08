from typing import List
import numpy as np

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Create a bit mask to limit k to the range [0, 2^maximumBit - 1]
        max_val = (1 << maximumBit) - 1
        
        # Compute prefix XOR for all elements in nums
        prefix_xor = np.cumsum(nums).view('u4')
        
        # Calculate the result array by applying XOR with max_val and reversing it
        result = ((prefix_xor ^ max_val) & max_val)[::-1]
        
        return result.tolist()