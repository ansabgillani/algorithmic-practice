class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction_index = 0
        max_distance = 0
        
        # Convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:  # Move forward
                dx, dy = directions[direction_index]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance