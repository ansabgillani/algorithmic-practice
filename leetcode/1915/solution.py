class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to store prefix XOR counts
        prefix_xors = {0: 1}
        count = xor = 0
        
        # Iterate over each character in the string
        for char in word:
            # Toggle the bit corresponding to the current character
            xor ^= 1 << (ord(char) - ord('a'))
            
            # Check all possible single odd occurrences
            for i in range(10):
                count += prefix_xors.get(xor ^ (1 << i), 0)
            
            # Add the count of substrings where exactly one character appears an odd number of times
            count += prefix_xors.get(xor, 0)
            
            # Update the prefix XOR counts dictionary
            prefix_xors[xor] = prefix_xors.get(xor, 0) + 1
        
        return count

# Example usage:
# solution = Solution()
# print(solution.wonderfulSubstrings("aba"))  # Output: 4