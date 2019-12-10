import tkinter as tk
import requests, json,math
from tkinter import *
from random import randint,choice
# uses the api of the site http://www.cs.utep.edu/cheon/ws/sudoku/ to generate puzzles

class myApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Sudoku")
        self.entries = {}
        self.exist = [[0 for i in range(9)] for j in range(9)]
        #sends a request for a puzzle with a random difficulty between 1 and 3
        board = requests.get(f"http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level={randint(1,3)}").json()
        #generates spots to enter numbers
        for j in range(9):
            self.entries[j]= {}
            for i in range(9):
                self.entries[j][i] = Lotfi(self,width=3,borderwidth=1, relief="solid")
                self.entries[j][i].configure(font=(20))

        #adds starting values and makes them uneditable. stores which spots have values to make clearing the board easy
        if(board["response"]):
            for x in board["squares"]:
                self.entries[x["x"]][x["y"]].insert(0,str(x["value"]))
                self.exist[x["x"]][x["y"]]=1
                self.entries[x["x"]][x["y"]].configure(state="readonly")

        #places entry spots in a grid
        for j in range(9):
            for i in range(9):
                self.entries[j][i].grid(row=j,column=i)

        self.labelText = StringVar()
        b1 = Button(self,text="Clear",command=self.clear)
        b2 = Button(self,text="Win check",width=7,compound=CENTER,command=self.win)
        l = Label(self,textvariable=self.labelText)
        b1.grid(row=9,column=5,columnspan=2,sticky=E)
        b2.grid(row=9,column=7,columnspan=2,ipadx=1,sticky=E)
        l.grid(row=9,column=0,columnspan=4,sticky=W)
        self.setStatus("Incomplete")

    #Clears all entries
    def clear(self):
        for j in range(9):
            for i in range(9):
                if self.exist[j][i] != 1:
                    self.entries[j][i].delete(0,END)

    #Sets the status label
    def setStatus(self,status):
        self.labelText.set("Status: " + status)

    #Checks if you've won
    def win(self):
        for j in range(9):
            for i in range(9):
                if self.entries[j][i].get() == "" or self.entries[j][i].get() == None:
                    self.setStatus("Incomplete")
                    return
        for j in range(9):
            for i in range(9):
                for h in range(9):
                    if self.entries[j][i].get() == self.entries[j][h].get() and h!=i:
                        self.setStatus("Incorrect")
                        return
                    if self.entries[j][i].get() == self.entries[h][i].get()and h!=j:
                        self.setStatus("Incorrect")
                        return
                    if self.entries[j][i].get() == self.entries[math.floor(j/3)*3+math.floor(h/3)][math.floor(i/3)*3+math.floor(h%3)].get()and j!=math.floor(j/3)*3+math.floor(h/3)and i!=math.floor(i/3)*3+math.floor(h%3):
                        self.setStatus("Incorrect")
                        return
        self.setStatus("Complete")

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
