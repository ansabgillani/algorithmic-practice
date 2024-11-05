class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        changes = 0
        i = 0
        while i < n:
            if i + 1 < n and s[i] != s[i+1]:
                changes += 1
            i += 2
        return changes