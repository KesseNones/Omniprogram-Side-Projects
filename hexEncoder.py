from tkinter import *
import math
from math import log

class Hexa(object):
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
            font = "Ariel 45", command = self.decipher)
        self.convButtonII.grid(row = 1, column = 1)

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

    def encipher(self):
        entryString = self.msg.get()
        encodedString = ""
        for char in entryString:
            val = ord(char)
            hexVal = self.tenToOtherBase(val, 16)
            encodedString += hexVal + " "
        self.tOutput["text"] = encodedString
        self.copy(encodedString)
        return encodedString

    def decipher(self):
        entryString = self.msg.get()
        hexArr = entryString.split(" ")
        decodedString = ""
        for el in hexArr:
            dec = int(el, 16)
            char = chr(dec)
            decodedString += char
        self.tOutput["text"] = decodedString
        self.copy(decodedString)
        return decodedString


    def baseAlg(self, num, base):
        digitArr = []
        if num == 0:
            return ["0"]
        while num > 0:
            digitArr.append(str(num % base))
            num = num // base
        return digitArr

    def tenToOtherBase(self, num, base):
        convNum = str()
        if base < 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            for el in digits:
                convNum = convNum + el
        if base >= 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            letterDigits = self.toLetters(digits, base)
            for el in letterDigits:
                convNum = convNum + el
        return convNum

    def toLetters(self, digitArr, base):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        loc = 0
        for el in digitArr:
            if int(el) > 9:
                index = int(el) - 10
                el = letters[index]
                digitArr[loc] = el
            loc += 1
        return digitArr

    def quitButtonAction(self):
        self.window.destroy()

def main():
    root = Tk()
    root.title("Hexadecimal Encoder and Decoder")
    temp = Hexa(root)
    root.mainloop()

if __name__ == "__main__":
    main()
