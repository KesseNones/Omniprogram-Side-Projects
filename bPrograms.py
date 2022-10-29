from tkinter import *
#import winsound

class B(object):
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

        self.berButton = Button(self.frameBottom, text = "Bearimy Converter", 
            font = "Ariel 30", command = self.berimyConv)
        self.berButton.grid(row = 0, column = 0)

        self.baseConvButton = Button(self.frameBottom, text = "Base Converter", 
            font = "Ariel 30", command = self.baseConvert)
        self.baseConvButton.grid(row = 0, column = 1)

        self.binConvButton = Button(self.frameBottom, text = "Binary Encoder and Decoder", 
            font = "Ariel 30", command = self.binConv)
        self.binConvButton.grid(row = 0, column = 2)

        self.binClockButton = Button(self.frameBottom, text = "Binary Clock", 
            font = "Ariel 30", command = self.binClock)
        self.binClockButton.grid(row = 1, column = 0)

        self.binClockButton = Button(self.frameBottom, text = "Base Stopwatch", 
            font = "Ariel 30", command = self.anyBaseStop)
        self.binClockButton.grid(row = 1, column = 1)
        
        self.baseSixClockButton = Button(self.frameBottom, text = "Base Six Clock", 
            font = "Ariel 30", command = self.baseSixClock)
        self.baseSixClockButton.grid(row = 1, column = 2)
        
        self.baseCalcButton = Button(self.frameBottom, text = "Base Calculator", 
            font = "Ariel 30", command = self.baseCalculator)
        self.baseCalcButton.grid(row = 2, column = 0)

        self.baseSixClockButtonII = Button(self.frameBottom, text = "Base Six Clock V. II", 
            font = "Ariel 30", command = self.baseSixClock2)
        self.baseSixClockButtonII.grid(row = 2, column = 1)

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()

    def berimyConv(self):
        import bearimyConverterGUI
        #self.clickSound()
        bearimyConverterGUI.main()

    def baseConvert(self):
        import baseConvGui
        baseConvGui.main()

    def binConv(self):
        import binEncoder
        binEncoder.main()

    def binClock(self):
        import binaryClock
        binaryClock.main()

    def anyBaseStop(self):
        import baseCounter
        baseCounter.main()
        
    def baseSixClock(self):
        import baseSixClock
        baseSixClock.main()
        
    def baseCalculator(self):
        import baseCalculator
        baseCalculator.main()

    def baseSixClock2(self):
        import baseSixClock2
        baseSixClock2.main()

def main():
    root = Tk()
    root.title("Programs That Start With B")
    om = B(root)
    root.mainloop()

if __name__ == "__main__":
    main()