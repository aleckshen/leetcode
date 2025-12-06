class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return 
            
            board[r][c] = 'T'
            capture(r - 1, c) #top
            capture(r, c - 1) #left
            capture(r + 1, c) #bottom
            capture(r, c + 1) #right

        for c in range(cols):
            capture(0, c)
            capture(rows - 1, c)

        for r in range(rows):
            capture(r, 0)
            capture(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'