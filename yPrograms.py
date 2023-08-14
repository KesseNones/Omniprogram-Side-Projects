#Jesse A. Jones
#Version: 2023-08-14.92

from tkinter import *
import youtubeTierConv

#Holds programs that start with the letter Y.
class Y(object):
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

        self.youtubeButton = Button(self.frameBottom, text = "Youtube Tier Converter", 
            font = FONT, command = self.youtubeTier)
        self.youtubeButton.grid(row = 0, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def youtubeTier(self):          
        youtubeTierConv.main()

def main():
    root = Tk()
    root.title("Y Programs")
    om = Y(root)
    root.mainloop()

if __name__ == "__main__":
    main()