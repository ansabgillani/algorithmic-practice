class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Count the number of index pairs (i, j) such that i < j and 
        words[i] is both a prefix and suffix of words[j].
        
        :param words: List of strings to be evaluated
        :return: Number of valid index pairs
        """
        count = 0
        
        # Iterate over each pair of indices (i, j) where i < j
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                    count += 1
                    
        return count