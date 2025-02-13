from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        """
        Merges two lists of items where each item is represented as [value, weight].
        Returns a merged list with each value's total weight, sorted by value.
        
        :param items1: List[List[int]] - First list of items
        :param items2: List[List[int]] - Second list of items
        :return: List[List[int]] - Merged and sorted list of items
        """
        merged_weights = defaultdict(int)
        
        for value, weight in items1 + items2:
            merged_weights[value] += weight
        
        return sorted([[value, weight] for value, weight in merged_weights.items()])