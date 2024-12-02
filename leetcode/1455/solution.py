class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Check if searchWord is a prefix of any word in sentence.
        
        :param sentence: Sentence consisting of words separated by a single space.
        :param searchWord: Word to check as a prefix.
        :return: Index of the first word where searchWord is a prefix (1-indexed), or -1 if not found.
        """
        words = sentence.split()
        for index, word in enumerate(words):
            if word.startswith(searchWord):
                return index + 1
        return -1

# Test cases
print(Solution().isPrefixOfWord("i love eating burger", "burg"))  # Output: 4
print(Solution().isPrefixOfWord("this problem is an easy problem", "pro"))  # Output: 2
print(Solution().isPrefixOfWord("i am tired", "you"))  # Output: -1