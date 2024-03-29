#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import bigNumberUnderstander
import hexEncoder
import hexClock

#Contains programs that have titles starting with the letter H.
class H(object):
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
    
        self.bigNumButton = Button(self.frameBottom, text = "Huge Number Converter", 
            font = FONT, command = self.hugeNumber)
        self.bigNumButton.grid(row = 0, column = 0)

        self.hexButton = Button(self.frameBottom, text = "Hexadecimal Encoder", 
            font = FONT, command = self.hexCode)
        self.hexButton.grid(row = 0, column = 1)

        self.hexClockButton = Button(self.frameBottom, text = "Hexadecimal Clock", 
            font = FONT, command = self.hexClock)
        self.hexClockButton.grid(row = 0, column = 2)

    def quitButtonAction(self):
        self.window.destroy()

    def hugeNumber(self):                   
        bigNumberUnderstander.main()

    def hexCode(self):                      
        hexEncoder.main()

    def hexClock(self):                     
        hexClock.main()

def main():
    root = Tk()
    root.title("Programs that Start with H")
    om = H(root)
    root.mainloop()

if __name__ == "__main__":
    main()