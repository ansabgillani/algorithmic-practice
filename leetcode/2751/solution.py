class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i]) for i in range(n)]
        robots.sort()  # Sort by position
        stack = []

        for pos, health, direction in robots:
            if direction == 'R':
                stack.append((health, direction))
            else:  # direction == 'L'
                while stack and stack[-1][1] == 'R' and stack[-1][0] < health:
                    stack.pop()
                if not stack or stack[-1][1] == 'L':
                    stack.append((health - 1, direction))
                elif stack[-1][1] == 'R' and stack[-1][0] == health:
                    stack.pop()

        surviving_robots = sorted([(pos, health) for pos, health, _ in stack], key=lambda x: positions.index(x[0]))
        return [health for _, health in surviving_robots]