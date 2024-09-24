class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Finds the length of the longest common prefix between all pairs of integers (x, y)
        where x belongs to arr1 and y belongs to arr2.
        
        :param arr1: List of positive integers
        :param arr2: List of positive integers
        :return: Length of the longest common prefix among all pairs
        """
        # Convert lists to sets of strings for efficient lookup
        set1 = {str(num) for num in arr1}
        set2 = {str(num) for num in arr2}
        
        max_length = 0
        
        # Iterate through each number in set1 and check its prefixes against set2
        for num_str in set1:
            prefix_length = 0
            while prefix_length <= len(num_str):
                if num_str[:prefix_length+1] in set2:
                    prefix_length += 1
                else:
                    break
            max_length = max(max_length, prefix_length)
        
        return max_length