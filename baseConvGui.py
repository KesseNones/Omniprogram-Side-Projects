#Jesse A. Jones
#Version: 2023-08-01.26

from tkinter import *
import math
import dateHandling

#This class contains methods and members used 
#   to convert from base ten to bases 2-36, and vice versa.
class baseConv(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button and clear entries button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Times 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        #Clear button.
        self.clearButton = Button(self.frameTop, text = "Clear Entries",
            font = "Times 20", command = self.clear)
        self.clearButton.pack(side = LEFT)

        #Bottom frame holds all other entires and buttons.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        #Input for general integer.
        self.messageI = Label(self.frameBottom, text = "Enter Integer:", font = "Times 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.I = Entry(self.frameBottom, font = "Times 20")
        self.I.grid(row = 0, column = 1)

        #Slider to choose base from 2 to 36
        self.baseScalar = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 200, 
            label = "Base:", font = "Times 20", command = self.sliderNumber)
        self.baseScalar.grid(row = 1, column = 0)

        #Conversion to base ten button.
        self.customBaseConvButton = Button(self.frameBottom, text = "Convert from Custom Base", 
            font = "Times 20", command = self.anyBaseToTen)
        self.customBaseConvButton.grid(row = 2, column = 0)

        #Outputs conversion of specified base to base ten.
        self.baseTenOut = Entry(self.frameBottom, text = "", 
            font = "Times 20")
        self.baseTenOut.grid(row = 2, column = 1)

        #Input for a base ten specific integer.
        self.messageII = Label(self.frameBottom, text = "Enter Base Ten Integer:", font = "Times 20", anchor = "w")
        self.messageII.grid(row = 3, column = 0)
        self.bsTen = Entry(self.frameBottom, font = "Times 20")
        self.bsTen.grid(row = 3, column = 1)

        #Scale specifies what base to convert the input base ten integer to.
        self.baseScalarII = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 200, 
            label = "Base Type:", font = "Times 20", command = self.sliderNumberII)
        self.baseScalarII.grid(row = 4, column = 0)

        #Button calls function to convert base ten integert to another base.
        self.tenToOtherBaseButton = Button(self.frameBottom, text = "Convert to Different Base", 
            font = "Times 20", command = self.baseTenToSpecificBase)
        self.tenToOtherBaseButton.grid(row = 5, column = 0)

        #Displays outputed conversion of base ten to another base.
        self.baseNOut = Entry(self.frameBottom, text = "", 
            font = "Times 20")
        self.baseNOut.grid(row = 5, column = 1)

        self.parse = dateHandling.GetDate()

    #Clears input entries.
    def clear(self):
        self.I.delete(0, "end")
        self.bsTen.delete(0, "end")
        self.baseTenOut.delete(0, "end")
        self.baseNOut.delete(0, "end")

    #Converts custom base integer to base ten.
    def anyBaseToTen(self):
        baseTenInt = self.baseConvert(True)
        self.baseTenOut.delete(0, "end")
        self.baseTenOut.insert(0, f"Base 10: {baseTenInt}")

    #Converts a base ten integer to any base in range 2 to 36.
    def baseTenToSpecificBase(self):
        otherBaseInt = self.baseConvert(False)
        self.baseNOut.delete(0, "end")
        self.baseNOut.insert(0, f"Base {self.sliderNumberII(666)}: {otherBaseInt}")

    #Returns the present value of the first base slider.
    def sliderNumber(self, num):
        baseNum = int(self.baseScalar.get())
        return baseNum

    #Returns the value of the second base slider.
    def sliderNumberII(self, num2):
        baseNum = int(self.baseScalarII.get())
        return baseNum

    #Fetches string representation of integer passed in.
    def integerNum(self):
        return str(self.parse.getYear(self.I.get()))

    #Fetches base 10 integer from input.
    def baseTenInt(self):
        return self.parse.getYear(self.bsTen.get())

    #Converts either a base ten integer to another base, 
    #   or the otherway around, depending upon input boolean.
    def baseConvert(self, isTurningToDecimalOnly):
        if isTurningToDecimalOnly:
            #Gets slider value and input integer.
            num = self.integerNum()
            base = self.sliderNumber(666)
            
            #Built in int function converts input integer 
            #   to base 10 from input base.
            decnum = int(num, base)
            return decnum
        else:
            #Fetches base ten integer and slider of base conversion.
            numX = self.baseTenInt()
            base = self.sliderNumberII(666)

            #Converts base ten int to another base.
            convertedNum = self.tenToOtherBase(numX, base)
            return convertedNum

    #Creates array of digits representing each place in the converted number.
    def baseAlg(self, num, base):
        digitArr = []
        if num == 0:
            return ["0"]
        while num > 0:
            digitArr.append(str(num % base))
            num = num // base
        return digitArr

    #This function is the fucntion that actually 
    #   converts a base ten integer to another base.
    def tenToOtherBase(self, num, base):
        convNum = str()
        #Case where elements of number don't need to be turned to letters.
        if base < 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            #Builds number string from initial digit array.
            for el in digits:
                convNum = convNum + el

        #Case where some pieces of the number need to be turned into letters.
        if base >= 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            letterDigits = self.toLetters(digits, base)
            #Builds number string.
            for el in letterDigits:
                convNum = convNum + el
        return convNum

    #Converts numbers greater than nine to letters, 
    #   since our number system has no symbols 
    #   for numbers greater than 9.
    def toLetters(self, digitArr, base):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        loc = 0
        for el in digitArr:
            #Converts number greater than nine to a letter.
            if int(el) > 9:
                index = int(el) - 10
                el = letters[index]
                digitArr[loc] = el
            loc += 1
        return digitArr

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

def main():
    root = Tk()
    root.title("Base Converter")
    star = baseConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
