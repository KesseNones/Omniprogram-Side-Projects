#Jesse A. Jones
#Version: 2022-12-22.2

from tkinter import *
import baseConvertClass

#This class contains members and methods that transforms strings 
#   to binary chunks representing each character in the ASCII convention.
class Binar(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds input fields as well 
        #   as conversion button and output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #String/binary entry.
        self.message = Label(self.frameBottom, text = "Enter String:", font = "Times 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.msg = Entry(self.frameBottom, font = "Times 20")
        self.msg.grid(row = 0, column = 1)

        #Encryption button.
        self.convButtonI = Button(self.frameBottom, text = "Encrypt", 
            font = "Times 20", command = self.encipher)
        self.convButtonI.grid(row = 1, column = 0)

        #Decryption button.
        self.convButtonII = Button(self.frameBottom, text = "Decrypt", 
            font = "Ariel 20", command = self.decipher)
        self.convButtonII.grid(row = 1, column = 1)

        #Resulting conversion.
        self.message = Label(self.frameBottom, text = "Output:", font = "Times 20", anchor = "w")
        self.message.grid(row = 3, column = 0)
        self.tOutput = Entry(self.frameBottom, font = "Times 20")
        self.tOutput.grid(row = 3, column = 1)

        self.baseConv = baseConvertClass.BaseConvert()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Makes sure each byte is eight bits long. Adds leading zeroes.
    def formatByte(self, origNum):
        altNum = origNum
        fillerZero = "0"
        #Adds leading zeroes if needed.
        while (len(altNum) < 8):
            altNum = fillerZero + altNum
        return altNum

    #Turns text to binary.
    def encipher(self):
        #Acquires user input.
        entryString = self.msg.get()
        encodedString = ""

        #Extracts each character from the string, turns it 
        #   to its ASCII value, and converts the ASCII value to binary.
        for char in entryString:
            val = ord(char)
            binVal = self.baseConv.tenToOtherBase(val, 2)
            binVal = self.formatByte(binVal)
            encodedString += binVal + " "

        #Displays output binary to user.
        self.tOutput.delete(0, "end")
        self.tOutput.insert(0, encodedString)

    #Turns binary to text.
    def decipher(self):
        #Fetches user input binary string and checks for emptyness.
        entryString = self.msg.get()
        if (entryString == ""):
            decodedString = ""
            self.tOutput.delete(0, "end")
            self.tOutput.insert(0, decodedString)
            return

        #Splits up binary string, converts each byte 
        #   to characters and adds them to a decoded string.
        hexArr = entryString.split(" ")
        decodedString = ""
        for el in hexArr:
            dec = int(el, 2)
            char = chr(dec)
            decodedString += char

        #Displays decoded string to user.
        self.tOutput.delete(0, "end")
        self.tOutput.insert(0, decodedString)

def main():
    root = Tk()
    root.title("Binary Encoder and Decoder")
    temp = Binar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
