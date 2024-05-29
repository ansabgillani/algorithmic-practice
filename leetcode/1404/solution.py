class Solution:
    def numSteps(self, s: str) -> int:
        """
        Return the number of steps to reduce a binary number represented as a string 's' to 1.
        
        :param s: Binary number as a string
        :return: Number of steps required
        """
        # Convert binary string to integer
        num = int(s, 2)
        steps = 0
        
        while num > 1:
            if num % 2 == 0:
                # If even, divide by 2
                num //= 2
            else:
                # If odd, add 1
                num += 1
            steps += 1
        
        return steps