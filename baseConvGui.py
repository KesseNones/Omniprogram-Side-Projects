from tkinter import *
import math

class baseConv(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Times 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        self.clearButton = Button(self.frameTop, text = "Clear Entries",
            font = "Ariel 20", command = self.clear)
        self.clearButton.pack(side = LEFT)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        self.messageI = Label(self.frameBottom, text = "Enter Integer:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.I = Entry(self.frameBottom, font = "Times 55")
        self.I.grid(row = 0, column = 1)

        self.baseScalar = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 400, 
            label = "Base:", font = "Times 30", command = self.sliderNumber)
        self.baseScalar.grid(row = 1, column = 0)

        self.affButton = Button(self.frameBottom, text = "Convert from Custom Base", 
            font = "Times 40", command = self.anyBaseToTen)
        self.affButton.grid(row = 2, column = 0)

        self.aOutput = Label(self.frameBottom, text = "", 
            font = "Times 45")
        self.aOutput.grid(row = 2, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Base Ten Integer:", font = "Times 55", anchor = "w")
        self.messageII.grid(row = 3, column = 0)

        self.bsTen = Entry(self.frameBottom, font = "Times 55")
        self.bsTen.grid(row = 3, column = 1)

        self.baseScalarII = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 400, 
            label = "Base Type:", font = "Times 30", command = self.sliderNumberII)
        self.baseScalarII.grid(row = 4, column = 0)

        self.cButton = Button(self.frameBottom, text = "Convert to Different Base", 
            font = "Times 40", command = self.baseTenToSpecificBase)
        self.cButton.grid(row = 5, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 45")
        self.cOutput.grid(row = 5, column = 1)

    def clear(self):
        self.I.delete(0, "end")
        self.bsTen.delete(0, "end")

    def anyBaseToTen(self):
        self.bs_conv(2)
        self.aOutput["text"] = "Base Ten: " + str(float(self.decimalizedNum))

    def baseTenToSpecificBase(self):
        self.bs_conv(1)
        self.cOutput["text"] = self.out

    def sliderNumber(self):
        baseNum = int(self.baseScalar.get())
        return baseNum

    def sliderNumberII(self):
        baseNum = int(self.baseScalarII.get())
        return baseNum

    def integerNum(self):
        if self.I.get() == "":
            return 0
        return self.I.get()

    def baseTenInt(self):
        if self.bsTen.get() == "":
            return 0
        return int(self.bsTen.get())

    def bs_conv(self, ch):
    # Base Ten to Different Base System (1)
    # Any Base to Base Ten (2) 
        Choice = ch
        if Choice == 1:
            numX = self.baseTenInt()
            base = self.sliderNumberII()
            convertedNum = self.tenToOtherBase(numX, base)
            self.out = convertedNum
        if Choice == 2:
            numorig = self.integerNum()
            num = str(numorig)
            base = self.sliderNumber()
            decnum = int(num, base)
            self.decimalizedNum = decnum

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
    root.title("Base Converter")
    star = baseConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
