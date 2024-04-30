class Solution:
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  # Bitmask to track odd/even counts of characters
        count[0] = 1  # Initial state, empty string
        total_wonderful = 0
        current_mask = 0

        for char in word:
            current_mask ^= 1 << (ord(char) - ord('a'))  # Toggle bit for the character
            total_wonderful += count[current_mask]  # Add substrings with exactly one odd count

            # Check for any substring where at most one character has an odd count
            for i in range(10):
                total_wonderful += count[current_mask ^ (1 << i)]

        count[current_mask] += 1  # Update the count for this mask

        return total_wonderful