from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        size = len(board)

        # creating hashmap for rows and columns for checking the duplicates
        cols = defaultdict(set)
        rows = defaultdict(set)
        subGrids = defaultdict(set)     # here key = (rows / 3, cols / 3)()as it is (3x3)

        # print(rows, cols, subGrids)

        for row in range(size):
            for col in range(size):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in subGrids[(row // 3, col // 3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                subGrids[(row // 3, col // 3)].add(board[row][col])

        return True
