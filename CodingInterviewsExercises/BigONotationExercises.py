'Important note: the numbers always increase on the top to the bottom way and the left to the right way'
def count_negatives(numberMatrix):
    count = 0
    row_i = 0
    'catch the right corner of the matrix'
    col_i = len(numberMatrix[0]) - 1
    while col_i >= 0 and row_i < len(numberMatrix):
        if numberMatrix[row_i][col_i] < 0:
            count+= (col_i + 1)
            row_i += 1
        else:
            col_i -= 1

        return count



count_negatives([[-2,0],[-1,0]])