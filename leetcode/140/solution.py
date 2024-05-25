class Solution:
    def wordBreak(self, s: str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        from functools import lru_cache

        word_set = set(wordDict)
        
        @lru_cache(None)
        def backtrack(start):
            if start == len(s):
                return [""]
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub_sentence in backtrack(end):
                        result.append(word + (sub_sentence and " " + sub_sentence))
            return result
        
        return [sentence.strip() for sentence in backtrack(0)]

# Test cases
solution = Solution()

print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  # Output: ["cats and dog", "cat sand dog"]
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))  # Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: []