class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        Calculate the index of the person holding the pillow after a given time.
        
        :param n: Number of people in the line
        :param time: Time elapsed in seconds
        :return: Index of the person holding the pillow
        """
        # The pillow completes a full round every (n-1) * 2 seconds
        cycle_time = (n - 1) * 2
        
        # Reduce time by removing complete cycles
        effective_time = time % cycle_time
        
        # If within the first half of the cycle, calculate position directly
        if effective_time < n:
            return effective_time + 1
        
        # Otherwise, calculate position from the end of the line
        return (n - 1) * 2 - effective_time + 1

# Example usage:
sol = Solution()
print(sol.passThePillow(4, 5))  # Output: 2
print(sol.passThePillow(3, 2))  # Output: 3