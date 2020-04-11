import os
import shutil
import termfmt as tfmt

class TxtFmt:
    def __init__(self, t="", s=None):
        self.txt=t
        self.style=s

class XYTerm:
    def __init__(self):
        self.size=None
        self.resize()

    def resize(self):
        if self.size==shutil.get_terminal_size():
            return
        self.size=shutil.get_terminal_size()
        self.table=[[TxtFmt(" ") for c in range(self.size[0])] for l in range(self.size[1])]

    def getLine(self, l):
        curStyle=None
        ret=""
        for c in self.table[l]:
            if c.style!=curStyle:
                if c.style is None: ret+=tfmt.resetAll
                else: ret+=c.style
                curStyle=c.style
            ret+=c.txt
        return ret+tfmt.resetAll

    def display(self):
        for l in range(len(self.table)):
            print(self.getLine(l), end=("" if l==len(self.table)-1 else "\n"))

    def print(self, c, l, t):
        for txtfmt in t:
            for char in txtfmt.txt:
                if c>=self.size[1]: return
                self.table[l][c]=TxtFmt(char, txtfmt.style)
                c+=1

