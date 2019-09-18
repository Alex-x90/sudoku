import tkinter as tk
from tkinter import *
import math
from random import randint
from random import choice

class myApp(tk.Tk):                                             #exist and entries aren't defined
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        exist = [[0 for i in range(9)] for j in range(9)]
        entries = {}
        temp = [[randint(0,9) for i in range(9)] for j in range(9)]
        for j,row in enumerate(temp):
            entries[j]= {}
            for i,col in enumerate(row):
                if(col<4):
                    exist[j][i]=1
                else:
                    exist[j][i]=0
                entries[j][i] = Lotfi(self,width=3)
                entries[j][i].configure(font=(20))
                if(exist[j][i]):
                    entries[j][i].insert(0,str(choice([k for k in range(9) if k not in self.checkList(j,i)])))
                    entries[j][i].configure(state="readonly")
                entries[j][i].grid(row=j,column=i)

    #Returns an array of all values that would be in same "group" as the given coordinate
    def checkList(self,row,col):
        output=[]
        for x in range(9):
            if entries[row][x].get() != None:
                output.append(entries[row][x].get())
            if entries[x][col].get() != None:
                output.append(entries[x][col].get())
            if entries[math.floor(row/3)*3+math.floor(x/3)][math.floor(col/3)*3+math.floor(x%3)].get() != None:
                output.append(entries[math.floor(row/3)*3+math.floor(x/3)][math.floor(col/3)*3+math.floor(x%3)].get())
        return output

    #Clears all entries
    def clear(self):
        for j in range(9):
            for i in range(9):
                if exist[j][i] != 1:
                    entries[j][i].delete(0,END)
    #Checks if you've won
    def win():
        print("test")

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

app=myApp()
app.title("Sudoku")

b1 = Button(root,text="Clear",command=myApp.clear)
b2 = Button(root,text="Win check",command=myApp.win)

b1.grid(row=9,column=2,columnspan=2,sticky=E)
b2.grid(row=9,column=5,columnspan=2,sticky=E)

app.mainloop()
