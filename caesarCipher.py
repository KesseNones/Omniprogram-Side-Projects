#Jesse A. Jones
#Version: 2023-05-10.08

from tkinter import *

#This class takes in an input string and spits out a string 
#   where all non-number characters are shifted forward 
#   or back by an input number of letters.
class Caesar(object):
    #Creates GUI and stuff.
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button created.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds string input
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #String input zone created.
        self.message = Label(self.frameBottom, text = "Enter String:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.msg = Entry(self.frameBottom, font = "Ariel 20")
        self.msg.grid(row = 0, column = 1)

        #Forwards shifting button.
        self.convButtonI = Button(self.frameBottom, text = "Shift Forwards", 
            font = "Ariel 20", command = self.shiftForward)
        self.convButtonI.grid(row = 1, column = 0)

        #Backwards shifting button.
        self.convButtonII = Button(self.frameBottom, text = "Shift Backwards", 
            font = "Ariel 20", command = self.shiftBackward)
        self.convButtonII.grid(row = 1, column = 1)

        #Slider that specifies how much shift occurs.
        self.shiftLevel = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 0, to = 25, length = 400, 
            label = "Character Shift Amount:", font = "Ariel 20", command = self.shiftLevelGet)
        self.shiftLevel.grid(row = 2, column = 0)

        #Converted output.
        self.message = Label(self.frameBottom, text = "Output:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 3, column = 0)
        self.tOutput = Entry(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 1)

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Called when forward shift button is pressed.
    def shiftForward(self):
        self.shiftString(False)

    #Called when backward shift button is pressed.
    def shiftBackward(self):
        self.shiftString(True)

    #Gets shift level.
    def shiftLevelGet(self, lvl):
        return int(self.shiftLevel.get())

    #Updates output text.
    def setNewText(self, txt):
        self.tOutput.delete(0, "end")
        self.tOutput.insert(0, txt)
        self.tOutput.update()

    #Shifts an input character by +/- n
    #   if it's an upper or lowercase character.
    def shiftChar(self, c, n, isShiftingBack = False):
        #Used in shifting back versus forwards.
        posNegArr = [1, -1]

        #If the character is uppercase alphabet character, 
        #   then shift character forwards or backwards by n.
        if ord(c) in range(65,91):
            outC = ord(c) + (n * posNegArr[isShiftingBack])
            if outC > 90:
                outC -= 26
            if outC < 65:
                outC += 26
            outC = chr(outC)

        #If the character is lowercase alphabet character, 
        #   then shift character forwards or backwards by n.
        elif ord(c) in range(97,123):
            outC = ord(c) + (n * posNegArr[isShiftingBack])
            if outC > 122:
                outC -= 26
            if outC < 97:
                outC += 26
            outC = chr(outC)

        #If character is not uppercase or lowercase 
        #   alphabetical character, nothing happens to it.
        else:
            outC = c

        return outC

    #Shifts a string forwards or backwards.
    def shiftString(self, isShiftingBack = False):
        inputString = self.msg.get()
        displacement = int(self.shiftLevel.get())
        shiftedString = ""
        for c in inputString:
            shifted = self.shiftChar(c, displacement, isShiftingBack)
            shiftedString += shifted
        self.setNewText(shiftedString)

def main():
    root = Tk()
    root.title("Caesar Cipher Encoder and Decoder")
    temp = Caesar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
