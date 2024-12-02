class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for index, word in enumerate(words, start=1):
            if word.startswith(searchWord):
                return index
        return -1