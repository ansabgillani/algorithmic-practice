from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # Count occurrences of each digit
        count = Counter(num)
        
        # Handle the special case when all digits are '0'
        if count['0'] == len(num):
            return '0'
        
        left_half = []
        middle_digit = ''
        
        # Construct the left half of the palindrome
        for digit in "987654321":
            if count[digit] > 1:
                left_half.append(digit * (count[digit] // 2))
        
        # Add the largest possible single digit to the middle if any are available
        for digit in "9876543210":
            if count[digit] % 2 == 1:
                middle_digit = digit
                break
        
        # Construct the palindrome by concatenating left_half, middle_digit, and reverse of left_half
        result = ''.join(left_half) + middle_digit + ''.join(reversed(left_half))
        
        return result

# Example usage:
sol = Solution()
print(sol.largestPalindromic("444947137"))  # Output: "7449447"
print(sol.largestPalindromic("00009"))      # Output: "9"