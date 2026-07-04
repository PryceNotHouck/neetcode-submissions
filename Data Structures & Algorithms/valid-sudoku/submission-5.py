class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = defaultdict(list)
        colCheck = defaultdict(list)
        boxCheck = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rowCheck.get(r, []):
                    return False
                else:
                    rowCheck[r].append(board[r][c])

                if board[r][c] in colCheck.get(c, []):
                    return False
                else:
                    colCheck[c].append(board[r][c])

                if board[r][c] in boxCheck.get((r // 3, c // 3), []):
                    return False
                else:
                    boxCheck[(r // 3, c // 3)].append(board[r][c])

        return True