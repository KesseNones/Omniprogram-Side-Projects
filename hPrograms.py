from tkinter import *
#import winsound

class H(object):
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
    
        self.bigNumButton = Button(self.frameBottom, text = "Huge Number Converter", 
            font = "Ariel 30", command = self.hugeNumber)
        self.bigNumButton.grid(row = 0, column = 0)

        self.hexButton = Button(self.frameBottom, text = "Hexadecimal Encoder", 
            font = "Ariel 30", command = self.hexCode)
        self.hexButton.grid(row = 0, column = 1)

        self.hexClockButton = Button(self.frameBottom, text = "Hexadecimal Clock", 
            font = "Ariel 30", command = self.hexClock)
        self.hexClockButton.grid(row = 0, column = 2)

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()

    def hugeNumber(self):
        import bigNumberUnderstander
        #self.clickSound()
        bigNumberUnderstander.main()

    def hexCode(self):
        import hexEncoder
        hexEncoder.main()

    def hexClock(self):
        import hexClock
        hexClock.main()

def main():
    root = Tk()
    root.title("Programs that Start with H")
    om = H(root)
    root.mainloop()

if __name__ == "__main__":
    main()