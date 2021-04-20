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
    def creatListOfDomains(self):
        self.listOfDomain=list()
        for i in range(len(self.SudokuBoard)):
            for j in range(len(self.SudokuBoard[i])):
                if self.SudokuBoard[i][j]==0:
                    #find domain
                    totalDomain = {i for i in range(1, 10)}
                    for k in range(len(self.SudokuBoard[0])):
                        #check row
                        if self.SudokuBoard[i][k]!=0:
                            totalDomain.discard(self.SudokuBoard[i][k])
                        #check column
                        if  self.SudokuBoard[k][j]!=0:
                            totalDomain.discard(self.SudokuBoard[k][j])
                        #check 3*3 square
                    for m in range((i// 3) * 3, (i // 3) * 3 + 3):
                        for n in range((j// 3) * 3, (j // 3) * 3 + 3):
                            if self.SudokuBoard[m][n]!=0:
                                totalDomain.discard(self.SudokuBoard[m][n])
                    self.listOfDomain.append([i,j,[k for k in totalDomain]])
        #sort list of domains
        self.listOfDomain.sort(key=lambda k: len(k[2]))



    #changed part of simple backtracking algorithm
    def find_Next_EmptyCell(self):
        for i in self.listOfDomain:
            if self.SudokuBoard[i[0]][i[1]]==0:
                return (i[0],i[1],i[2])
        return None

#MRV algorithm
def cSP_MRV(board:Board):
    board.showSudoku()
    print("*****************************")
    unSolvedCell=board.find_Next_EmptyCell()
    if unSolvedCell==None :
        return True
    else:
        if(len(unSolvedCell[2])==0):
            return False
        for i in unSolvedCell[2]:
            board.changeCell(unSolvedCell[0],unSolvedCell[1],i)
            board.creatListOfDomains()
            #next step in search
            if cSP_MRV(board):
                return True
            #Backtrack and assign another number
            else:
                board.changeCell(unSolvedCell[0],unSolvedCell[1],0)
                board.creatListOfDomains()
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
test.creatListOfDomains()
#test.showSudoku()
if cSP_MRV(test):
    print("sudoko solved")
else:
    print("failed")


