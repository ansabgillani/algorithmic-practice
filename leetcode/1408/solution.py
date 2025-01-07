class Solution:
    def stringMatching(self, words):
        words.sort(key=len)
        
        result = []
        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                if word1 in word2:
                    result.append(word1)
                    break
                    
        return result