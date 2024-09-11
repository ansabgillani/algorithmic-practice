class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR start and goal to find differing bits
        xor_result = start ^ goal
        # Count the number of set bits (1s) in the XOR result
        bit_count = bin(xor_result).count('1')
        return bit_count

# Test cases
sol = Solution()
print(sol.minBitFlips(10, 7))  # Output: 3
print(sol.minBitFlips(3, 4))   # Output: 3