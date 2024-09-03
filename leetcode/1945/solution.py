class Solution:
    def getLucky(self, s, k):
        num = int(''.join(str(ord(c) - 96) for c in s))
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))
        return num

# Test cases
print(Solution().getLucky("iiii", 1))  # Output: 36
print(Solution().getLucky("leetcode", 2))  # Output: 6
print(Solution().getLucky("zbax", 2))  # Output: 8