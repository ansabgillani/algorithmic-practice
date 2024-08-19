class Solution:
    def minSteps(self, n: int) -> int:
        """
        Returns the minimum number of operations to get exactly n 'A's on the screen.
        
        :param n: The target number of 'A's.
        :return: Minimum number of operations required.
        """
        if n == 1:
            return 0
        
        result = n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                result = min(result, self.minSteps(i) + n // i)
                break
        
        return result