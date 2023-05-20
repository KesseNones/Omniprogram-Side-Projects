#Jesse A. Jones
#Version: 2023-05-20.95

from tkinter import *
from random import choice

#This class generates an alias for Kesse Nones 
#   to use for one of its incarnations.
class KesseNamGen(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds alias generation button and text output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Generates alias for Kesse Nones when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Generate Alias", 
            font = "Ariel 30", command = self.nameGen)
        self.convButtonI.grid(row = 0, column = 0)

        #Kesse Nones alias output text.
        self.message = Label(self.frameBottom, text = "Name:", font = "Ariel 30", anchor = "w")
        self.message.grid(row = 1, column = 0)
        self.tOutput = Label(self.frameBottom, text = "Kesse Nones", 
            font = "Ariel 30", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 2, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Generates Kesse Nones alias and displays result.
    def nameGen(self):
        alphaArr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]

        #Randomly picks first letter of each name chunk.
        firstWordIndex = choice(range(0, 27))
        secondWordIndex = choice(range(0, 27))
        
        #Derives chars to be added to alias string.
        firstChar = alphaArr[firstWordIndex]
        secondChar = alphaArr[secondWordIndex]

        #Builds and displays alias string.
        alias = firstChar + "esse " + secondChar + "ones" 
        self.tOutput["text"] = alias

def main():
    root = Tk()
    root.title("Kesse Nones Alias Generator")
    temp = KesseNamGen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
