class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in "123456789":
            if self.is_valid(board, row, col, num):
                board[row][col] = num

                if self.solve(board):
                    return True

                board[row][col] = '.'

        return False

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def is_valid(self, board, row, col, num):
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False

        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False

        # Check box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True