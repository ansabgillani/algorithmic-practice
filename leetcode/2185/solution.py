class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Returns the number of strings in words that contain pref as a prefix.
        
        :param words: List of strings to search through
        :param pref: The prefix to look for
        :return: Count of words with the given prefix
        """
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

# Test cases
print(Solution().prefixCount(["pay", "attention", "practice", "attend"], "at"))  # Output: 2
print(Solution().prefixCount(["leetcode", "win", "loops", "success"], "code"))  # Output: 0