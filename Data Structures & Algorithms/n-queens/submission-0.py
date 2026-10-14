class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]    # creating empty board
        # print(board) 
        ans = []

        # trackers
        left_row = [0] * n                    # rows
        lower_diag = [0] * (2 * n - 1)        # r + c
        upper_diag = [0] * (2 * n - 1)        # (n-1) + c - r  -> shift to [0..2n-2]
        
        # print(left_row)
        # print(lower_diag)
        # print(upper_diag)
        
        def solve(col):
            if col == n:
                ans.append([''.join(r) for r in board])
                return
            
            for row in range(n):
                ld = row + col
                ud = (n - 1) + col - row

                if left_row[row] == 0 and lower_diag[ld] == 0 and upper_diag[ud] == 0:
                    board[row][col] = 'Q'
                    left_row[row] = 1
                    lower_diag[ld] = 1
                    upper_diag[ud] = 1

                    solve(col + 1)

                    # Now delete the placed 'Q' for next queen check
                    board[row][col] = '.'
                    left_row[row] = 0
                    lower_diag[ld] = 0
                    upper_diag[ud] = 0
            
        solve(0)
        return ans
            