#Jesse A. Jones
#Version: 2023-06-13.19

from tkinter import *
import youtubeTierConv

#Holds programs that start with the letter Y.
class Y(object):
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

        self.youtubeButton = Button(self.frameBottom, text = "Youtube Tier Converter", 
            font = "Ariel 30", command = self.youtubeTier)
        self.youtubeButton.grid(row = 0, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def youtubeTier(self):          #DONE
        youtubeTierConv.main()

def main():
    root = Tk()
    root.title("Y Programs")
    om = Y(root)
    root.mainloop()

if __name__ == "__main__":
    main()