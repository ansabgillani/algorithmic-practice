class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        
        def dfs(x, y, index):
            if index == len(word) - 1:
                return True
            
            temp, board[x][y] = board[x][y], '/'
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == word[index + 1]:
                    if dfs(nx, ny, index + 1):
                        return True
            
            board[x][y] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                    
        return False