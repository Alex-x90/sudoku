import tkinter as tk
from tkinter import *
import math
from random import randint
from random import choice

class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set
    def check(self, *args):
        if self.get() is "":
            # the current value is empty; allow this
            self.old_value = self.get()
        elif self.get().isdigit():
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)
        if len(self.get())>1 : self.set(self.get()[:1])

def checkList(row,col): #DOESNT WORK PROPERLY
    output=[]
    for x in range(9):
        if values[row][col] == values[row][x] and values[row][x] != None:
            output.append(values[row][x])
        if values[row][col] == values[x][col] and values[x][col] != None:
            output.append(values[x][row])
        if values[row][col] == values[math.floor(row/3)+math.floor(x/3)][math.floor(col/3)+math.floor(x%3)] and values[math.floor(row/3)+math.floor(x/3)][math.floor(col/3)+math.floor(x%3)] != None:
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

values = [[None for i in range(9)] for j in range(9)]

for j in range(9):
    for i in range(9):
        if(exist[j][i]):
            print(checkList(j,i))
            temp = choice([k for k in range(0,9) if k not in checkList(j,i)])
            print(temp)
            values[j][i]=temp
            # values[j][i]=choice([i for i in range(0,9) if i not in checkList(j,i)])


root=tk.Tk()
root.title("Sudoku")

entries = {}
for j in range(9):
    entries[j]= {}
    for i in range(9):
        entries[j][i] = Lotfi(root,width=3)
        if values[j][i] is not None:
            entries[j][i].insert(0,str(values[j][i]))
            entries[j][i].configure(state="readonly")

for j in range(9):
    for i in range(9):
        entries[j][i].grid(row=j,column=i)

root.mainloop()
