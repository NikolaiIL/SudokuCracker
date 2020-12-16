# from BacktrackingSudoku import isValid, solveSudokuHelper
from helper import solve_sudoku

# Enter your Sudoku here!
board=[
    [0,0,0,1,5,0,0,0,0],
    [5,0,8,0,0,4,0,1,0],
    [1,0,4,0,8,0,0,0,3],
    [0,0,7,0,0,6,5,4,0],
    [8,0,0,0,2,0,9,0,7],
    [0,0,0,0,3,0,0,0,2],
    [0,8,0,5,0,0,0,9,0],
    [9,1,6,0,4,3,8,0,0],
    [0,0,0,0,0,7,0,0,0]]
solve_sudoku(0,0,board)