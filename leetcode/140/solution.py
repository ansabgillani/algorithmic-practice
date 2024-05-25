class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(start=0):
            if start == len(s): 
                return ['']
            res = []
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in self.word_set:
                    for sentence in backtrack(end):
                        res.append(prefix + ' ' + sentence)
            return res

        # Convert the word dictionary to a set for O(1) average time complexity lookups
        self.word_set = set(wordDict)
        
        # Start backtracking from the beginning of the string
        return [sentence.strip() for sentence in backtrack()]