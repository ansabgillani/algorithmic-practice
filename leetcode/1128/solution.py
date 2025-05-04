from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Create a dictionary to count occurrences of normalized domino tuples
        domino_count = defaultdict(int)
        
        # Normalize each domino by sorting the pair and use it as a key in the dictionary
        for a, b in dominoes:
            normalized_domino = tuple(sorted([a, b]))
            domino_count[normalized_domino] += 1
        
        # Calculate the number of equivalent pairs using combinations
        num_pairs = 0
        for count in domino_count.values():
            if count > 1:
                # Number of ways to choose 2 items from 'count' is given by combination formula: n * (n - 1) // 2
                num_pairs += count * (count - 1) // 2
        
        return num_pairs