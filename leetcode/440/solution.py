class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count numbers in lexicographical order starting from 'current' and having 'digits'
        def countNumbers(current, digits):
            count = 0
            nextCurrent = current + 1
            while current <= n:
                count += min(n + 1, nextCurrent) - current
                if count >= k:
                    return True
                current *= 10
                nextCurrent *= 10
                digits -= 1
                if digits == 0:
                    break
            return False

        # Start from the first number 1
        current = 1
        while k > 1:
            # If we can reach at least 'k' numbers starting from 'current'
            if countNumbers(current, len(str(n))):
                k -= 1
            else:
                k -= countNumbers(0, 0)
                current += 1
        return current

# Test cases
print(Solution().findKthNumber(13, 2))  # Output: 10
print(Solution().findKthNumber(1, 1))   # Output: 1