class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        
        # Define the target state and directions (up, down, left, right)
        target = '123450'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Convert the board to a string for easier manipulation
        initial_state = ''.join(str(num) for row in board for num in row)
        
        # If the initial state is already the target, return 0 moves
        if initial_state == target:
            return 0
        
        # Initialize the queue with the initial state and move count
        queue = deque([(initial_state, 0)])
        visited = set([initial_state])
        
        while queue:
            current_state, moves = queue.popleft()
            
            # Find the position of the empty space (0)
            i, j = next((i, j) for i in range(2) for j in range(3) if current_state[i * 3 + j] == '0')
            
            # Try moving the empty space in all four directions
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < 2 and 0 <= nj < 3:
                    new_state = list(current_state)
                    new_state[i * 3 + j], new_state[ni * 3 + nj] = new_state[ni * 3 + nj], new_state[i * 3 + j]
                    new_state = ''.join(new_state)
                    
                    if new_state == target:
                        return moves + 1
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, moves + 1))
        
        # If the target state is not reachable, return -1
        return -1