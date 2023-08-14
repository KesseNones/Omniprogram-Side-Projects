#Jesse A. Jones
#Version: 2023-08-14.92

from tkinter import *
import kardeshevCalcGUI
import kessNonesAliasGen

class K(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        FONT = "Ariel 20"

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = FONT, command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.connecButton = Button(self.frameBottom, text = "Kardeshev Calc", 
            font = FONT, command = self.karCalc)
        self.connecButton.grid(row = 0, column = 0)

        self.connecButton = Button(self.frameBottom, text = "Kesse Nones Alias Generator", 
            font = FONT, command = self.kesseNonesAlias)
        self.connecButton.grid(row = 0, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def karCalc(self):                  
        kardeshevCalcGUI.main()

    def kesseNonesAlias(self):          
        kessNonesAliasGen.main()

def main():
    root = Tk()
    root.title("Programs that Start with K")
    om = K(root)
    root.mainloop()

if __name__ == "__main__":
    main()