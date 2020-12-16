import numpy as np

def is_in_xRow(yValue,candidate,matrix):
    for xRowValue in range(9):
        if matrix[yValue][xRowValue] == candidate:
            return True
    return False

def is_in_yRow(xValue, candidate, matrix):
    for yRowValue in range(9):
        if matrix[yRowValue][xValue] == candidate:
            return True
    return False

def is_in_block(yValue, xValue, candidate, matrix):
    initialValueY = yValue-yValue%3
    initialValueX = xValue-xValue%3
    for checkedYValue in range( initialValueY,  initialValueY+3):
        for checkedXValue in range(initialValueX, initialValueX+3):
            if matrix[checkedYValue][checkedXValue] == candidate:
                return True
    return False

def is_valid_number(yValue, xValue, candidate, matrix):
    if is_in_xRow(yValue,candidate,matrix):
        return False
    if is_in_yRow(xValue, candidate, matrix):
        return False
    if is_in_block(yValue, xValue, candidate, matrix):
        return False
    return True
    
def solve_sudoku(yValue, xValue, matrix):
    if xValue == 8 and yValue == 8:
        if matrix[yValue][xValue] != 0:
            print(matrix)
        else:
            for number in range(1,10):
                if is_valid_number(yValue, xValue, number, matrix):
                    matrix[yValue][xValue]=number
                    print(np.matrix(matrix))
                    matrix[yValue][xValue]=0
        return
    if xValue > 8:
        solve_sudoku(yValue + 1, 0, matrix)
        return
    if matrix[yValue][xValue] == 0:
        for number in range(1,10):
            if is_valid_number(yValue, xValue, number, matrix):
                matrix[yValue][xValue] = number
                solve_sudoku(yValue, xValue + 1, matrix)
                matrix[yValue][xValue] = 0
    else:
        solve_sudoku(yValue, xValue + 1, matrix)
    return