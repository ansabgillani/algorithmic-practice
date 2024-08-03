from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Determine if two arrays can be made equal by reversing subarrays.
        
        :param target: Target array to achieve.
        :param arr: Initial array to transform.
        :return: True if possible, otherwise False.
        """
        # Check if the frequency of each element in both arrays is the same
        return Counter(target) == Counter(arr)