class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb to the nth stair.
        
        :param n: The total number of stairs.
        :return: The number of distinct ways to reach the nth stair.
        """
        if n <= 1:
            return 1
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Test cases
solution = Solution()
print(solution.climbStairs(1))  # Output: 1
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(4))  # Output: 5