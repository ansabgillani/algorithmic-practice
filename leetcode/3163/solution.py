class Solution:
    def compress(self, word: str) -> str:
        """
        Compresses a string by removing prefixes of characters repeating at most 9 times and appending the length followed by the character.
        
        Args:
        word (str): The input string to be compressed.
        
        Returns:
        str: The compressed string.
        """
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            char = word[i]
            count = 1
            
            # Count the length of the current character prefix
            while i + 1 < n and word[i + 1] == char and count < 9:
                i += 1
                count += 1
            
            # Append the count followed by the character to the compressed string
            comp += str(count) + char
            
            i += 1
        
        return comp

# Example usage:
sol = Solution()
print(sol.compress("abcde"))  # Output: "1a1b1c1d1e"
print(sol.compress("aaaaaaaaaaaaaabb"))  # Output: "9a5a2b"