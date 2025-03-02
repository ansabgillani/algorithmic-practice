from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """
        Merges two arrays of items by summing the weights of similar items.
        
        :param items1: First list of items, where each item is [value_i, weight_i]
        :param items2: Second list of items, where each item is [value_i, weight_i]
        :return: A merged list of items sorted by value
        """
        # Create a dictionary to store the total weight for each unique value
        value_to_weight = defaultdict(int)
        
        # Sum weights for items in the first list
        for value, weight in items1:
            value_to_weight[value] += weight
        
        # Sum weights for items in the second list
        for value, weight in items2:
            value_to_weight[value] += weight
        
        # Convert the dictionary to a sorted list of [value, weight]
        return sorted([[value, weight] for value, weight in value_to_weight.items()])