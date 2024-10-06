class Solution:
    def areSentencesSimilarIII(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1) > len(words2):
            words1, words2 = words2, words1

        i, j = 0, len(words2) - 1
        
        while i < len(words1) and words1[i] == words2[i]:
            i += 1

        while j >= 0 and words1[-(j + 1)] == words2[j]:
            j -= 1

        return i > j