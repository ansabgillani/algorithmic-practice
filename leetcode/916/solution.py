class Solution:
    def wordSubsets(self, A, B):
        # Create a counter for the maximum frequency of each character in any string in B
        max_b_count = Counter()
        for b in B:
            max_b_count |= Counter(b)
        
        # Filter words in A that have at least the same frequency of characters as max_b_count
        universal_words = []
        for a in A:
            if Counter(a) >= max_b_count:
                universal_words.append(a)
        
        return universal_words