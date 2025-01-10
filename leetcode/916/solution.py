from collections import Counter, defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Function to get the character count of a word
        def char_count(word):
            return Counter(word)
        
        # Merge counts from multiple words into one
        def merge_counts(counts):
            merged = Counter()
            for count in counts:
                merged += count
            return merged
        
        # Get the maximum required character count from words2
        b_max = merge_counts([char_count(b) for b in words2])
        
        # Check if a word in words1 is universal
        def is_universal(word):
            return all(word.count(c) >= cnt for c, cnt in b_max.items())
        
        # Return list of universal words from words1
        return [word for word in words1 if is_universal(word)]