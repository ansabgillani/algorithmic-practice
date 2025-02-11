class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "")
        return s

# Test cases
solution = Solution()
print(solution.removeOccurrences("daabcbaabcbc", "abc"))  # Output: "dab"
print(solution.removeOccurrences("axxxxyyyyb", "xy"))     # Output: "ab"