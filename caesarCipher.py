from tkinter import *
import math
from math import log

class Caesar(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter String:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.msg = Entry(self.frameBottom, font = "Times 50")
        self.msg.grid(row = 0, column = 1)

        self.convButtonI = Button(self.frameBottom, text = "Encrypt", 
            font = "Ariel 45", command = self.encipher)
        self.convButtonI.grid(row = 1, column = 0)

        self.convButtonII = Button(self.frameBottom, text = "Decrypt", 
            font = "Ariel 45", command = self.decipherEasy)
        self.convButtonII.grid(row = 1, column = 1)

        self.shiftLevel = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 0, to = 25, length = 400, 
            label = "Character Shift Amount:", font = "Times 30", command = self.shiftLevelGet)
        self.shiftLevel.grid(row = 2, column = 0)

        self.message = Label(self.frameBottom, text = "Output:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 3, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 3, column = 1)

    def copy(self, string):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(string)
        clip.destroy()

    def quitButtonAction(self):
        self.window.destroy()

    def shiftLevelGet(self):
        return int(self.shiftLevel.get())

    def shift(self, c, n):
        """
        Helper method that shifts all alpabetical characters by 
        the specified number.
        """
        if ord(c) in range(65,91):
            outC = ord(c) + n
            #If the number code of the character is in the upper case range,
            # the following if statements will be run and
            # the output character will be declared, which  
            # will be the input character increased by the specified number.
            if outC > 90:
                outC -= 26
                #If the output character goes beyond the capital range,
                # it has 26 subtracted to wrap it to the other side.
                # For example, an outC of "Z" + 1 would yield "A" 
            if outC < 65:
                outC += 26
                #If the output character goes beyond the capital range
                # in the other direction,
                # it has 26 added to wrap it to the other side.
                # For example, an outC of "A" - 1 would yield "Z"
            outC = chr(outC)
            #Output character set back to character string.
        elif ord(c) in range(97,123):
            outC = ord(c) + n
            #If the number code of the character is in the lower case range,
            # the following if statements will be run and
            # the output character will be declared, which  
            # will be the input character increased by the specified number.
            if outC > 122:
                outC -= 26
                #If the output character goes beyond the lowercase range,
                # it has 26 subtracted to wrap it to the other side.
                # For example, an outC of "z" + 1 would yield "a"
            if outC < 97:
                #If the output character goes beyond the lowercase range
                # in the other direction,
                # it has 26 added to wrap it to the other side.
                # For example, an outC of "a" - 1 would yield "z"
                outC += 26
            outC = chr(outC)
            #Output character set back to character string.
        else:
            outC = c
            #If the character is not alphabetical in nature,
            # it is returned as is.
        return outC
        #The output character is returned.
    def backShift(self, c, n):
        """
        Helper method that shifts all alpabetical characters by 
        the specified number, but the other direction.
        """
        if ord(c) in range(65,91):
            #If the number code of the character is in the upper case range,
            # the following if statements will be run and
            # the output character will be declared, which  
            # will be the input character increased by the specified number.
            outC = ord(c) - n
            if outC > 90:
                outC -= 26
                #If the output character goes beyond the capital range,
                # it has 26 subtracted to wrap it to the other side.
                # For example, an outC of "A" - 1 would yield "Z" 
            if outC < 65:
                outC += 26
                #If the output character goes beyond the capital range
                # in the other direction,
                # it has 26 added to wrap it to the other side.
                # For example, an outC of "Z" + 1 would yield "A"
            outC = chr(outC)
            #Output character set back to character string.
        elif ord(c) in range(97,123):
            #If the number code of the character is in the lower case range,
            # the following if statements will be run and
            # the output character will be declared, which  
            # will be the input character increased by the specified number.
            outC = ord(c) - n
            if outC > 122:
                outC -= 26
                #If the output character goes beyond the capital range,
                # it has 26 subtracted to wrap it to the other side.
                # For example, an outC of "a" - 1 would yield "z"
            if outC < 97:
                outC += 26
                #If the output character goes beyond the capital range
                # in the other direction,
                # it has 26 added to wrap it to the other side.
                # For example, an outC of "z" + 1 would yield "a"
            outC = chr(outC)
            #Output character set back to character string.
        else:
            outC = c
            #If the character is not alphabetical in nature,
            # it is returned as is.
        return outC
        #The output character is returned.
    def encipher(self):
        """
        Method takes an input string and uses the helper shift method
        to shift each alphabetical character a certain number of places,
        in order to encript it.
        """
        inputString = self.msg.get()
        displacement = int(self.shiftLevel.get())
        encodedString = ""
        for c in inputString:
            shifted = self.shift(c, displacement)
            encodedString += shifted
            #Iterates through each character in the input string,
            # calling the shift function to shift each character 
            # by the specified number of places inputed in main().
            # Each altered character is then concactinated 
            # to the encodedString variable, creating the encoded string.
        self.tOutput["text"] = encodedString
        self.copy(encodedString) 
    def decipherEasy(self):
        """
        This method uses the backShift helper method 
        to decode each character in the encodedString variable,
        taking in the number of times the characters were shifted 
        to encript the input string in the first place.
        The Result: a decrypted string that is the same as the input.  
        """
        encodedString = self.msg.get()
        displacement = int(self.shiftLevel.get())
        decodedString = ""
        for c in encodedString:
            backShifted = self.backShift(c, displacement)
            decodedString += backShifted
            #Iterates through each character in the encrypted string,
            # calling the backShift function to shift each character back
            # to their origional spots by the specified number 
            # of places inputed in main().
            # Each altered character is then concactinated 
            # to the decodedString variable, creating the decoded string.
        self.tOutput["text"] = decodedString
        self.copy(decodedString)
def main():
    root = Tk()
    root.title("Caesar Cipher Encoder and Decoder")
    temp = Caesar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
