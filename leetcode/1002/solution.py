from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the count of characters to be the minimum count from all words
        result_count = Counter(words[0])
        
        # Iterate over each word and update the result_count with the minimum character counts
        for word in words[1:]:
            result_count &= Counter(word)
            
        # Return the list of characters with their respective counts
        return list(result_count.elements())