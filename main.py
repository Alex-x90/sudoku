import tkinter as tk
from tkinter import *
import math
from random import randint
from random import choice

#status message chaging unfinished
#win check not finished
#buttons don't align properly

class myApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Sudoku")
        self.entries = {}
        self.exist = [[0 for i in range(9)] for j in range(9)]
        temp = [[randint(0,9) for i in range(9)] for j in range(9)]
        for j,row in enumerate(temp):
            self.entries[j]= {}
            for i,col in enumerate(row):
                if(col<4):
                    self.exist[j][i]=1
                else:
                    self.exist[j][i]=0
                self.entries[j][i] = Lotfi(self,width=3,borderwidth=1, relief="solid")
                self.entries[j][i].configure(font=(20))
        for j in range(9):
            for i in range(9):
                if(self.exist[j][i]):
                    self.entries[j][i].insert(0,str(choice([k for k in range(9) if k not in self.checkList(j,i)])))
                    self.entries[j][i].configure(state="readonly")
                self.entries[j][i].grid(row=j,column=i)
        b1 = Button(self,text="Clear",command=self.clear)
        b2 = Button(self,text="Win check",command=self.win,width=7)
        l = Label(self,text="Status: Incomplete")
        b1.grid(row=9,column=5,columnspan=2,sticky=E)
        b2.grid(row=9,column=7,columnspan=2)
        l.grid(row=9,column=0,columnspan=4)
    #Returns an array of all values that would be in same "group" as the given coordinate
    def checkList(self,row,col):
        output=[]
        for x in range(9):
            if self.entries[row][x].get() != None:
                output.append(self.entries[row][x].get())
            if self.entries[x][col].get() != None:
                output.append(self.entries[x][col].get())
            if self.entries[math.floor(row/3)*3+math.floor(x/3)][math.floor(col/3)*3+math.floor(x%3)].get() != None:
                output.append(self.entries[math.floor(row/3)*3+math.floor(x/3)][math.floor(col/3)*3+math.floor(x%3)].get())
        return output

    #changes status message
    def setStatus(self):

    #Clears all entries
    def clear(self):
        for j in range(9):
            for i in range(9):
                if self.exist[j][i] != 1:
                    self.entries[j][i].delete(0,END)
    #Checks if you've won
    def win(self):
        temp=False
        for j in range(9):
            for i in range(9):
                if self.entries[j][i].get() == "":
                    temp=True

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
app.mainloop()
