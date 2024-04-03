class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            temp, board[i][j] = board[i][j], '#'  # Mark as visited
            found = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = temp  # Backtrack
            
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False