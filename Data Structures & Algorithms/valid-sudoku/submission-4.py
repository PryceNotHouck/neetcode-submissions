class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colCheck = {}
        for r in range(len(board)):
            rowCheck = set()
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rowCheck:
                    return False
                else:
                    rowCheck.add(board[r][c])

                if colCheck.get((c, board[r][c]), False):
                    return False
                else:
                    colCheck[(c, board[r][c])] = True

        boxCheck = set()
        for rowBound in range(3, len(board) + 1, 3):
            for colBound in range(3, len(board) + 1, 3):
                for r in range(rowBound - 3, rowBound):
                    for c in range(colBound - 3, colBound):
                        if board[r][c] == '.':
                            continue
                        
                        if board[r][c] in boxCheck:
                            return False
                        else:
                            boxCheck.add(board[r][c])
                boxCheck = set()

        return True