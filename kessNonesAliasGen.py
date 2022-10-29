from tkinter import *
import math
from math import log
from random import choice

class KesseNamGen(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.convButtonI = Button(self.frameBottom, text = "Generate Alias", 
            font = "Times 45", command = self.nameGen)
        self.convButtonI.grid(row = 0, column = 0)

        self.message = Label(self.frameBottom, text = "Name:", font = "times 55", anchor = "w")
        self.message.grid(row = 1, column = 0)

        self.tOutput = Label(self.frameBottom, text = "Kesse Nones", 
            font = "Times 50", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 1, column = 1)

    def copy(self, string):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(string)
        clip.destroy()

    def quitButtonAction(self):
        self.window.destroy()

    def nameGen(self):
        alphaArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]
        firstWordIndex = choice(range(0, 27))
        secondWordIndex = choice(range(0, 27))
        firstChar = alphaArr[firstWordIndex]
        secondChar = alphaArr[secondWordIndex]
        alias = firstChar + "esse " + secondChar + "ones" 
        self.tOutput["text"] = alias
        self.copy(alias)

    def quitButtonAction(self):
        self.window.destroy()

def main():
    root = Tk()
    root.title("Kesse Nones Alias Generator")
    temp = KesseNamGen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
