from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Calculate the time taken for the person initially at position k to finish buying tickets.
        
        Args:
        tickets (List[int]): A list where tickets[i] is the number of tickets the i-th person wants to buy.
        k (int): The initial position of the person in the queue.
        
        Returns:
        int: The time taken for the person at position k to finish buying tickets.
        """
        time_taken = 0
        n = len(tickets)
        
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time_taken += 1
                if tickets[k] == 0:
                    break
        
        return time_taken

# Example usage:
# solution = Solution()
# print(solution.timeRequiredToBuy([2,3,2], 2))  # Output: 6
# print(solution.timeRequiredToBuy([5,1,1,1], 0))  # Output: 8