class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(x for row in board for x in row)
        if start == target:
            return 0
        
        neighbors = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            current_state, steps = queue.popleft()
            
            zero_index = current_state.index(0)
            for neighbor in neighbors[zero_index]:
                new_state = list(current_state)
                new_state[neighbor], new_state[zero_index] = new_state[zero_index], new_state[neighbor]
                new_state_tuple = tuple(new_state)
                
                if new_state_tuple == target:
                    return steps + 1
                
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state_tuple, steps + 1))
        
        return -1