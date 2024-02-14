from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearranges the elements of the given array such that every consecutive pair of integers have opposite signs,
        and the order of integers with the same sign is preserved. The rearranged array begins with a positive integer.
        
        :param nums: List[int] - Input list containing an equal number of positive and negative integers
        :return: List[int] - Rearranged list satisfying the conditions
        """
        pos = deque([x for x in nums if x > 0])
        neg = deque([x for x in nums if x < 0])
        
        result = []
        while pos or neg:
            if len(result) % 2 == 0:
                result.append(pos.popleft())
            else:
                result.append(neg.popleft())
        
        return result