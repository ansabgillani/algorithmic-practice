from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Finds all starting indices of substrings in 's' that is a concatenation of each word in 'words'.
        """
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = num_words * word_length
        word_count = defaultdict(int)
        
        for word in words:
            word_count[word] += 1
        
        result = []
        
        for i in range(len(s) - total_length + 1):
            seen = defaultdict(int)
            for j in range(num_words):
                word_index = i + j * word_length
                word = s[word_index:word_index + word_length]
                
                if word not in word_count:
                    break
                
                seen[word] += 1
                
                if seen[word] > word_count[word]:
                    break
            
            if seen == word_count:
                result.append(i)
        
        return result