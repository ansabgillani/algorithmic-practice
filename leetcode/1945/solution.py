class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert string to integer by replacing each letter with its position in the alphabet
        num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        
        # Transform the integer by summing its digits repeatedly k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        return int(num_str)

# Example usage:
solution = Solution()
print(solution.getLucky("iiii", 1))  # Output: 36
print(solution.getLucky("leetcode", 2))  # Output: 6
print(solution.getLucky("zbax", 2))  # Output: 8