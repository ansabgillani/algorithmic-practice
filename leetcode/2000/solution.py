class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        Reverses the segment of 'word' that starts at index 0 and ends at the first occurrence of 'ch'.
        If 'ch' does not exist in 'word', returns the original string.
        
        :param word: The input string to process.
        :param ch: The character to find the first occurrence of and reverse up to.
        :return: The resulting string after reversing the segment if 'ch' is found, otherwise the original string.
        """
        try:
            idx = word.index(ch)
            return word[:idx + 1][::-1] + word[idx + 1:]
        except ValueError:
            return word