#Jesse A. Jones
#Version: 2022-11-16.2

from tkinter import *
from random import choice

#This class contains the methods necessary to generate a random combination 
#   of alien sounding name pieces that 
#   are concatenated together to get an alienesque name.
class NamGen(object):
    #Sets up Tkinter window and appropriate buttons.
    def __init__(self, window = None):
        #Top frame containing quit button.
        self.window = window
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame and converstion button.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
        self.convButtonI = Button(self.frameBottom, text = "Generate Name", 
            font = "Ariel 45", command = self.nameGen)
        self.convButtonI.grid(row = 0, column = 0)

        #Alien name output.
        self.message = Label(self.frameBottom, text = "Name:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 1, column = 0)
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 1, column = 1)

        self.copyNameToClipBoard = False

    #If class variable set to true, this function 
    #   copies the generated alien name to the user's clipboard.
    def copy(self, string):
        if (self.copyNameToClipBoard):
            clip = Tk()
            clip.withdraw()
            clip.clipboard_clear()
            clip.clipboard_append(string)
            clip.destroy()

    #Quits given program instance.
    def quitButtonAction(self):
        self.window.destroy()

    #Generates random alien sounding name.
    def nameGen(self):
        firstSegArr = ["Gor", "Spea", "Ar", "Vol", "Mel", "Ter", "Kek", "Teal", "Ozge", "Kre", "Mor", "So", "Fel", "Yan", "Toq", "Krak", "Kess", "Kell", "Kror", "Wor", "Skek", "Tp'"]
        secondSegArr = ["sel", "krek", "eoru", "tek", "'", "arau", "bos","basil", "nel", "fu", "a", "or", "vi", "pur", "gar", "pol", "snor", "ron", "mort", "yuv", "frar", "t'rar", "wё", "osgalet", ""]
        thirdSegArr = ["orot", "'bel","ol", "nel", "kron", "org", "sen", "unal", "yun", "schek", "vek", "", "c"]
        firstIndex = choice(range(0, len(firstSegArr)))
        secondIndex = choice(range(0, len(secondSegArr)))
        thirdIndex = choice(range(0, len(thirdSegArr)))
        alienName = firstSegArr[firstIndex] + secondSegArr[secondIndex] + thirdSegArr[thirdIndex]
        self.tOutput["text"] = alienName
        self.copy(alienName)

def main():
    root = Tk()
    root.title("Alien Name Generator")
    temp = NamGen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
