
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
            total += matrix[i][i]

    return total

diagonal_sum([[1,0],[0,1]])

def rooks_are_safe(chessboard):
    n = len(chessboard)

    for row_i in range(n):
        rowCount = 0
        for  col_i in range(n):
            rowrowCount += chessboard[row_i][col_i]

        if rowCount > 1:
            return False

    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col_i]
            if col_count > 1:
                return False
    return True

rooks_are_safe([[0,0,0],[1,0,1],[0,0,0]])