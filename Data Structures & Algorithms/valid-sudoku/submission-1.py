class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        the most intuative sol seems to be checking if a already counter number exists
        in the row/col or 9 x 9
        make a dict out of each col, row and 9 x 9
        make sure each counter is one
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqs = collections.defaultdict(set)
        print(rows)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c]
                    or board[r][c] in sqs[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqs[(r // 3, c // 3)].add(board[r][c])
        return True