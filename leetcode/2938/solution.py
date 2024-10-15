class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        Return the minimum number of steps to group all black balls to the right and all white balls to the left.
        
        :param s: 0-indexed binary string of length n
        :return: Minimum number of steps required
        """
        n = len(s)
        ans = 0
        count_ones = 0
        
        for i in range(n):
            if s[i] == '1':
                count_ones += 1
            else:
                ans += i - count_ones
        
        return ans

# Test cases to validate the solution
print(Solution().minimumSteps("101"))    # Output: 1
print(Solution().minimumSteps("100"))    # Output: 2
print(Solution().minimumSteps("0111"))   # Output: 0