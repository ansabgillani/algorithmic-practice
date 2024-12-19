class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Split the array into chunks such that sorting each chunk individually and concatenating them results in a sorted array.
        
        :param arr: List of integers representing a permutation of [0, n - 1]
        :return: The largest number of chunks we can make to sort the array
        """
        max_chunk = 0
        current_max = 0
        
        for i, num in enumerate(arr):
            current_max = max(current_max, num)
            if current_max == i:
                max_chunk += 1
                
        return max_chunk