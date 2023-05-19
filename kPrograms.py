#Jesse A. Jones
#Version: 2023-05-19.98

from tkinter import *

class K(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 30", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.connecButton = Button(self.frameBottom, text = "Kardeshev Calc", 
            font = "Ariel 30", command = self.karCalc)
        self.connecButton.grid(row = 0, column = 0)

        self.connecButton = Button(self.frameBottom, text = "Kesse Nones Alias Generator", 
            font = "Ariel 30", command = self.kesseNonesAlias)
        self.connecButton.grid(row = 0, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def karCalc(self):                  #HERE
        import kardeshevCalcGUI
        kardeshevCalcGUI.main()

    def kesseNonesAlias(self):
        import kessNonesAliasGen
        kessNonesAliasGen.main()

def main():
    root = Tk()
    root.title("Programs that Start with K")
    om = K(root)
    root.mainloop()

if __name__ == "__main__":
    main()