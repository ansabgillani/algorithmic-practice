class Solution:
    def maxUniqueSplit(self, s):
        def backtrack(start, path):
            if start == len(s):
                return len(path)
            
            max_unique = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in path:
                    max_unique = max(max_unique, backtrack(end, path | {substring}))
        
            return max_unique
        
        return backtrack(0, set())