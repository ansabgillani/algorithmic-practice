class Solution:
    def compressStringIII(self, word):
        """
        Compresses a string using a custom algorithm.

        Args:
            word (str): The input string to be compressed.

        Returns:
            str: The compressed version of the input string.
        """

        comp = ''
        i = 0

        while i < len(word):

            # Find the length of the current character's repeating sequence
            count = 1
            while i + count < len(word) and word[i + count] == word[i]:
                count += 1
            
            # Append the count followed by the character to the compressed string
            if count > 1:
                comp += str(count)
            
            comp += word[i]
        
            # Move past the current sequence
            i += count

        return comp