class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, unique):
            if start == len(s):
                return len(unique)
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in unique:
                    unique.add(substring)
                    max_splits = max(max_splits, backtrack(end, unique))
                    unique.remove(substring)
            return max_splits
        
        return backtrack(0, set())