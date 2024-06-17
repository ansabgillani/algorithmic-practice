class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Determines if there are two integers a and b such that a^2 + b^2 = c.
        
        :param c: Non-negative integer
        :return: True if such a and b exist, False otherwise
        """
        left, right = 0, int(c**0.5)
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        return False

# Test cases
print(Solution().judgeSquareSum(5))  # Output: True
print(Solution().judgeSquareSum(3))  # Output: False