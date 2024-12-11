class Solution:
    def fib(self, n: int) -> int:
        """
        Returns the nth Fibonacci number using an iterative approach.
        
        Args:
        n (int): The position in the Fibonacci sequence.
        
        Returns:
        int: The nth Fibonacci number.
        """
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Test cases to validate the solution
assert Solution().fib(2) == 1
assert Solution().fib(5) == 5
assert Solution().fib(7) == 13
assert Solution().fib(0) == 0