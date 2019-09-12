import tkinter
from tkinter import *
import math
from random import randint
from random import choice

def checkList(row,col):
    output=[]
    for x in range(9):
        if values[row][col] == None:
            continue
        if values[row][col] == values[0][x]:
            output.append(values[0][x])
        if values[row][col] == values[x][0]:
            output.append(values[x][0])
        if values[row][col] == values[math.floor(row/3)+math.floor(x/3)][math.floor(col/3)+math.floor(x%3)]:
            output.append(values[math.floor(row/3)+math.floor(x/3)][math.floor(col/3)+math.floor(x%3)])
    return output

temp = [[randint(0,9) for i in range(9)] for j in range(9)]
exist = [[0 for i in range(9)] for j in range(9)]

for j,row in enumerate(temp):
    for i,col in enumerate(row):
        if(col<4):
            exist[j][i]=1
        else:
            exist[j][i]=0

temp=None
values = [[None for i in range(9)] for j in range(9)]

for j in range(9):
    for i in range(9):
        if(exist[j][i]):
            values[i][j]=choice([i for i in range(0,9) if i not in checkList(j,i)])


root=tkinter.Tk()
root.title("Sudoku")
for i in range(81):
    globals()["E".join(i)] = #CONSTRUCT ENTRY
root.mainloop()
