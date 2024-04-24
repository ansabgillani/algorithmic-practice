class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Compute the n-th Tribonacci number using dynamic programming.
        
        Args:
        n (int): The position in the Tribonacci sequence to compute.
        
        Returns:
        int: The n-th Tribonacci number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        # Initialize the first three Tribonacci numbers
        a, b, c = 0, 1, 1
        
        # Compute the n-th Tribonacci number iteratively
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c