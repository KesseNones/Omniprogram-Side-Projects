from tkinter import *
import math
from math import log

class StrRev(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter String:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.msg = Entry(self.frameBottom, font = "Times 50")
        self.msg.grid(row = 0, column = 1)

        self.convButtonI = Button(self.frameBottom, text = "Reverse", 
            font = "Ariel 45", command = self.reverse)
        self.convButtonI.grid(row = 1, column = 0)

        self.message = Label(self.frameBottom, text = "Output:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 3, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 3, column = 1)

    def copy(self, string):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(string)
        clip.destroy()

    def quitButtonAction(self):
        self.window.destroy()

    def reverse(self):
        entryString = self.msg.get()
        revString = entryString[::-1]
        self.copy(revString)
        self.tOutput["text"] = revString
        return revString

    def quitButtonAction(self):
        self.window.destroy()

def main():
    root = Tk()
    root.title("String Reverser")
    temp = StrRev(root)
    root.mainloop()

if __name__ == "__main__":
    main()
