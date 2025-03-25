class Solution:
    def canCutGrid(self, n: int, rectangles: List[List[int]]) -> bool:
        # Check for horizontal cuts
        x_coords = set()
        for rect in rectangles:
            if rect[1] == 0 and rect[3] == n:
                x_coords.update(range(rect[0], rect[2]))
        
        if len(x_coords) >= 2:
            return True
        
        # Check for vertical cuts
        y_coords = set()
        for rect in rectangles:
            if rect[0] == 0 and rect[2] == n:
                y_coords.update(range(rect[1], rect[3]))
        
        if len(y_coords) >= 2:
            return True
        
        return False

# Test cases
sol = Solution()
print(sol.canCutGrid(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))  # Output: True
print(sol.canCutGrid(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))  # Output: True
print(sol.canCutGrid(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))  # Output: False