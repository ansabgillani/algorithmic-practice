from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Finds all strings in 'words' that are a substring of another word.
        
        Args:
        words (List[str]): A list of unique strings.
        
        Returns:
        List[str]: A list of strings that are substrings of another string in 'words'.
        """
        # Create a set to store the result for O(1) average-time complexity lookups
        result_set = set()
        
        # Sort words by length to ensure shorter words are checked first
        words.sort(key=len)
        
        n = len(words)
        
        # Iterate over each word and check if any other word contains it as a substring
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    result_set.add(words[i])
                    break
        
        return list(result_set)

# Example usage:
sol = Solution()
print(sol.stringMatching(["mass", "as", "hero", "superhero"]))  # Output: ["as", "hero"]
print(sol.stringMatching(["leetcode", "et", "code"]))  # Output: ["et", "code"]
print(sol.stringMatching(["blue", "green", "bu"]))  # Output: []