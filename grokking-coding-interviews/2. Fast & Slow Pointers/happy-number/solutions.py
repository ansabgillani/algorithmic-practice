class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is a happy number.
        
        :param n: The integer to check.
        :return: True if n is a happy number, False otherwise.
        """
        def get_next(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit * digit
                num //= 10
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# Test cases
solution = Solution()

print(solution.isHappy(19))  # Output: True
print(solution.isHappy(2))   # Output: False