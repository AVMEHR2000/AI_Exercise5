import random
import math
import numpy as np
class Board:
    def __init__(self,ListOfElements):
        self.SudokuBoard=ListOfElements
    #this method changes the value of a specific cell in board
    def changeCell(self,raw,column,number):
        self.SudokuBoard[raw][column]=number
    #this method prints the board
    def showSudoku(self):
        for i in range(len(self.SudokuBoard)):
            if(i%3==0 ):
                print("- - - - - - - - - - - - - ")
            for j in range(len(self.SudokuBoard[i])):
                if(j%3==0):
                    print('|',end=' ')
                if(j==8):
                    print(str(self.SudokuBoard[i][j])+' |')
                else:
                    print(str(self.SudokuBoard[i][j]) + ' ',end='')
    def find_Next_EmptyCell(self):
        for i in range(len(self.SudokuBoard)):
            for j in range(len(self.SudokuBoard[i])):
                if self.SudokuBoard[i][j]==0:
                    return i,j #row and column of the next empty cell
        return None
    def check_constraints_forCell(self,number,pos):
        for i in range(len(self.SudokuBoard[0])):
            # check row
            if self.SudokuBoard[pos[0]][i]==number and pos[1]!=i:
                return False
            #check column
            if self.SudokuBoard[i][pos[1]]==number and pos[0]!=i:
                return False
        #check 3*3 squares
        for i in range((pos[0]//3)*3,(pos[0]//3)*3+3):
            for j in range((pos[1] // 3) * 3, (pos[1] // 3) * 3 + 3):
                if self.SudokuBoard[i][j] == number and pos != (i,j) :
                    return False

        return True

def cSP_SimpleBacktracking(board:Board):
    board.showSudoku()
    print("*****************************")
    unSolvedCell=board.find_Next_EmptyCell()
    if unSolvedCell==None:
        return True
    else:
        for i in range(1,10):
            if board.check_constraints_forCell(i,unSolvedCell):
                board.changeCell(unSolvedCell[0],unSolvedCell[1],i)
                #next step in search
                if cSP_SimpleBacktracking(board):
                    return True
                #Backtrack and assign another number
                else:
                    board.changeCell(unSolvedCell[0],unSolvedCell[1],0)
        return False



firstBoard=[[0,2,0,0,0,0,0,0,0],
            [0,0,0,6,0,0,0,0,3],
            [0,7,4,0,8,0,0,0,0],
            [0,0,0,0,0,3,0,0,2],
            [0,8,0,0,4,0,0,1,0],
            [6,0,0,5,0,0,0,0,0],
            [0,0,0,0,1,0,7,8,0],
            [5,0,0,0,0,9,0,0,0],
            [0,0,0,0,0,0,0,4,0]]

test=Board(firstBoard)
if cSP_SimpleBacktracking(test):
    print("sudoko solved")
else:
    print("failed")

