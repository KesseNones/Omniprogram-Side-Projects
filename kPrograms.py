from tkinter import *
#import winsound

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

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()

    def karCalc(self):
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