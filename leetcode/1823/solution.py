class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize a list to represent the circle of friends
        friends = list(range(1, n + 1))
        
        # Start at the first friend
        index = 0
        
        # Continue until only one friend remains
        while len(friends) > 1:
            # Calculate the index of the friend to be removed
            index = (index + k - 1) % len(friends)
            # Remove the friend from the circle
            friends.pop(index)
        
        # Return the last remaining friend
        return friends[0]