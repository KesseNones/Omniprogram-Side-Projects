from tkinter import *
#import winsound

class C(object):
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

        self.flipButton = Button(self.frameBottom, text = "Coin Flipper",
            font = "Ariel 30", command = self.coinFlipper)
        self.flipButton.grid(row = 0, column = 0)

        self.CButton = Button(self.frameBottom, text = "C to Warp Converter", 
            font = "Ariel 30", command = self.CToWarp)
        self.CButton.grid(row = 0, column = 1)

        self.connecButton = Button(self.frameBottom, text = "Connect Four", 
            font = "Ariel 30", command = self.connecFour)
        self.connecButton.grid(row = 0, column = 2)

        self.chiButton = Button(self.frameBottom, text = "Chinese Year Calculator", 
            font = "Ariel 30", command = self.chineseCalc)
        self.chiButton.grid(row = 1, column = 0)

        self.grdButton = Button(self.frameBottom, text = "Calculate Weighted Grade Not GUI", 
            font = "Ariel 30", command = self.grdCalc)
        self.grdButton.grid(row = 1, column = 1)

        self.calButton = Button(self.frameBottom, text = "Calendar Month Displayer", 
            font = "Ariel 30", command = self.mnthCalc)
        self.calButton.grid(row = 1, column = 2)

        self.caeButton = Button(self.frameBottom, text = "Caesar Cipher", 
            font = "Ariel 30", command = self.caesarCode)
        self.caeButton.grid(row = 2, column = 0)

        self.cenButton = Button(self.frameBottom, text = "Centaurian Time", 
            font = "Ariel 30", command = self.centaurian)
        self.cenButton.grid(row = 2, column = 1)
        
    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()
    
    def coinFlipper(self):
        import coinFlipGUI
        #self.clickSound()
        coinFlipGUI.main()

    def CToWarp(self):
        import betterCToWarpConv
        #self.clickSound()
        betterCToWarpConv.main()

    def connecFour(self):
        import connecFour
        #self.clickSound()
        connecFour.main()

    def chineseCalc(self):
        import chineseCalCalc
        chineseCalCalc.main()

    def grdCalc(self):
        import gradeCalc
        gradeCalc.main()

    def mnthCalc(self):
        import calMonthDisplayGUI
        calMonthDisplayGUI.main()

    def caesarCode(self):
        import caesarCipher
        caesarCipher.main()

    def centaurian(self):
        import centaurianTime
        centaurianTime.main()

def main():
    root = Tk()
    root.title("Programs That Start With C")
    om = C(root)
    root.mainloop()

if __name__ == "__main__":
    main()