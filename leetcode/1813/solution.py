class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # If the sentences are already equal, they are similar
        if words1 == words2:
            return True
        
        len1, len2 = len(words1), len(words2)
        
        # Ensure that words1 is the shorter sentence for consistency
        if len1 > len2:
            words1, words2 = words2, words1
            len1, len2 = len2, len1
        
        # Check similarity from both ends towards the center
        i, j = 0, 0
        while i < len1 and words1[i] == words2[j]:
            i += 1
            j += 1
        
        k, l = len1 - 1, len2 - 1
        while k >= 0 and words1[k] == words2[l]:
            k -= 1
            l -= 1
        
        # If all elements from both ends match, they are similar
        return i > k or j < l

# Test cases to ensure the solution works as expected
assert Solution().areSentencesSimilar("My name is Haley", "My Haley") == True
assert Solution().areSentencesSimilar("of", "A lot of words") == False
assert Solution().areSentencesSimilar("Eating right now", "Eating") == True