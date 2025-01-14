class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'  # Mark as visited
            
            found = (dfs(r + 1, c, k + 1) or
                    dfs(r - 1, c, k + 1) or
                    dfs(r, c + 1, k + 1) or
                    dfs(r, c - 1, k + 1))
            
            board[r][c] = temp  # Unmark
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

# Example usage:
solution = Solution()
print(solution.exist([
    ["A", "B", "C", "E"], 
    ["S", "F", "C", "S"], 
    ["A", "D", "E", "E"]
], "ABCCED"))  # Output: true