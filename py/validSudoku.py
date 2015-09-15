"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rowDicts = []
    colDicts = []
    gridDicts = []
    for i in range(0,10):
        rowDicts.append({})
        colDicts.append({})
        gridDicts.append({})
    for rowIndex, row in enumerate(board):
        for colIndex, val in enumerate(row):
            if val != '.':
                if val not in rowDicts[rowIndex]:
                    rowDicts[rowIndex][val] = True
                else:
                    return False
                if val not in colDicts[colIndex]:
                    colDicts[colIndex][val] = True
                else:
                    return False
                if val not in gridDicts[int(rowIndex/3) + (int(colIndex/3)*3)]:
                    gridDicts[int(rowIndex/3) + (int(colIndex/3)*3)][val] = True
                else:
                    return False
    return True
        