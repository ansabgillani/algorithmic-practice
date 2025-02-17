from collections import Counter
from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Returns the number of possible non-empty sequences of letters that can be made using the letters printed on the given tiles.
        """
        result = set()
        
        # Generate all permutations of lengths from 1 to len(tiles)
        for r in range(1, len(tiles) + 1):
            for perm in permutations(tiles, r):
                # Add unique permutations to the result set
                result.add(''.join(perm))
                
        return len(result)

# Example usage:
# sol = Solution()
# print(sol.numTilePossibilities("AAB"))  # Output: 8
# print(sol.numTilePossibilities("AAABBC"))  # Output: 188
# print(sol.numTilePossibilities("V"))  # Output: 1