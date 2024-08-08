class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        result = [(r0, c0)]
        dr, dc = 0, 1  # Initial direction is east

        for s in range(1, 2 * (R + C), 2):  # Total steps to move, increases by two each spiral layer
            for _ in range(s // 2):  # Move s/2 steps in the current direction
                r0 += dr
                c0 += dc
                if 0 <= r0 < R and 0 <= c0 < C:
                    result.append((r0, c0))
                    
            # Change direction clockwise: east -> south -> west -> north
            dr, dc = dc, -dr

        return result