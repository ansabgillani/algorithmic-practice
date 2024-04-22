from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends to a set for O(1) lookups
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        # Initialize the queue with the starting state and the number of moves
        queue = deque([("0000", 0)])
        # Use a set to keep track of visited states
        visited = {"0000"}
        
        while queue:
            current, moves = queue.popleft()
            
            if current == target:
                return moves
            
            for i in range(4):
                for d in [-1, 1]:
                    new_digit = (int(current[i]) + d) % 10
                    new_state = current[:i] + str(new_digit) + current[i+1:]
                    
                    if new_state not in visited and new_state not in deadends:
                        visited.add(new_state)
                        queue.append((new_state, moves + 1))
        
        return -1