class Solution:
    def robotSim(self, commands, obstacles):
        obstacle_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        x, y = 0, 0
        max_distance = 0
        
        for command in commands:
            if command == -2:
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:
                direction_idx = (direction_idx + 1) % 4
            else:
                dx, dy = directions[direction_idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                    else:
                        break
                
                max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance