class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        Finds the largest positive integer k such that -k also exists in the array.
        
        :param nums: List of integers without zeros
        :return: Largest positive integer k if it exists, otherwise -1
        """
        num_set = set(nums)
        max_k = -1
        
        for num in num_set:
            if -num in num_set and abs(num) > max_k:
                max_k = abs(num)
        
        return max_k