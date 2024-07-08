class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        index = 0
        
        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)
        
        return friends[0]