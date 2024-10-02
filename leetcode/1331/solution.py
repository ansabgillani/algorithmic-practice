class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Replaces each element in the array with its rank.
        
        The rank is determined by the value of the element,
        where larger values have higher ranks. Equal values receive the same rank,
        and the rank is minimized.
        
        :param arr: List of integers
        :return: List of integers representing the rank of each element in the input array
        """
        # Create a sorted list of unique elements
        sorted_unique = sorted(set(arr))
        
        # Create a dictionary to map each unique element to its rank
        rank_map = {value: index + 1 for index, value in enumerate(sorted_unique)}
        
        # Replace each element in the original array with its rank
        return [rank_map[value] for value in arr]