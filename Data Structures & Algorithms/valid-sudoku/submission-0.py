class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        board_check = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                board_index = (i // 3) * 3 + (j // 3)

                if (val in row_check[i] or
                    val in col_check[j] or 
                    val in board_check[board_index]):
                    return False
                row_check[i].add(val)
                col_check[j].add(val)
                board_check[board_index].add(val)
        return True

            