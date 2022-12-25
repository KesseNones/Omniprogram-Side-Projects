#Jesse A. Jones
#Version: 2022-12-25.1

from tkinter import *
import baseConvertClass

#This class contains fields and methods necessary for a calculator 
#   to calculate the four basic calculator operations for bases 2 through 36.
#Floating points are still a bit weird 
#   and the calculator doesn't like numbers too big or small.
class BaseCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button, clear button, and repeat calculation button.
        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column= 0)
        
        #Clear button.
        self.clearButton = Button(self.frameTop, text = "Clear",
            font = "Ariel 20", command = self.clear)
        self.clearButton.grid(row = 0, column= 1)
        
        #Calculation repetition button.
        self.repeatButton = Button(self.frameTop, text = "Repeat Calculation",
            font = "Ariel 20", command = self.repeat)
        self.repeatButton.grid(row = 0, column= 2)

        #Bottom frame holds number inputs, calculation output, and base slider.
        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 1, column = 0)

        #First number input.
        self.messageI = Label(self.frameBottom, text = "First Input:", font = "Times 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.first = Entry(self.frameBottom, font = "Times 20")
        self.first.grid(row = 1, column = 0)

        #Second number input.
        self.messageII = Label(self.frameBottom, text = "Second Input:", font = "Times 20", anchor = "w")
        self.messageII.grid(row = 3, column = 0)
        self.second = Entry(self.frameBottom, font = "Times 20")
        self.second.grid(row = 4, column = 0)

        #Base slider from base 2 to 36.
        self.baseScalar = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 300, 
            label = "Base:", font = "Times 20", command = self.sliderNumber)
        self.baseScalar.grid(row = 5, column = 0)

        #True bottom frame holds the four operation buttons 
        #   and the calculation output. 
        self.frameRockBottom = Frame(self.window)
        self.frameRockBottom.grid(row = 1, column = 1)

        #Add operation button.
        self.addButton = Button(self.frameRockBottom, text = "Add", 
            font = "Times 20", command = self.add)
        self.addButton.grid(row = 0, column = 0)
        
        #Subtraction operation button.
        self.subtractButton = Button(self.frameRockBottom, text = "Sub", 
            font = "Times 20", command = self.subtract)
        self.subtractButton.grid(row = 0, column = 1)
        
        #Multiply operation button.
        self.multiplyButton = Button(self.frameRockBottom, text = "Mult", 
            font = "Times 20", command = self.multiply)
        self.multiplyButton.grid(row = 1, column = 0)
        
        #Division operation button.
        self.divideButton = Button(self.frameRockBottom, text = "Div", 
            font = "Times 20", command = self.divide)
        self.divideButton.grid(row = 1, column = 1)

        #Calculation output.
        self.calcOutput = Entry(self.frameBottom, font = "Times 20")
        self.calcOutput.grid(row = 7, column = 0)
        
        #Used to track output number and action to be performed.
        self.resultNum = ""
        self.actionType = -1

        #Object instance used for converting between bases.
        self.baseConvert = baseConvertClass.BaseConvert()

    #Repeats a particular calculation, replacing the first number 
    #   with the previous calculation result.
    def repeat(self):
        self.first.delete(0, "end")
        self.first.insert(0, self.resultNum)

        #Determines which operation is called again.
        if (self.actionType == 0):
            self.add()
        elif (self.actionType == 1):
            self.subtract()
        elif (self.actionType == 2):
            self.multiply()
        else:
            self.divide()

    #Clears all entries and resets data.
    def clear(self):
        self.resultNum = ""
        self.actionType = 0
        self.first.delete(0, "end")
        self.second.delete(0, "end")
        self.calcOutput.delete(0, "end")

    #Used to do light input parsing of text from given field.
    def inputFetch(self, inp):
        if inp == "":
            return "0"
        else:
            return inp
    
    #Returns the two potentially floating 
    #   point input fields converted to base ten.
    #Returns array of converted number floating points on success.
    def inputParse(self):
        #Input base and fields acquired.
        base = int(self.baseScalar.get())
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())

        #Whole number and fraction fetched for each number.
        numArrFirst = self.antiFloatAlgorithim(first, base)
        numArrSecond = self.antiFloatAlgorithim(second, base)

        #First and second floating point numbers derived via fraction division.
        firstFloat = numArrFirst[0] + (numArrFirst[1] / (numArrFirst[2] + (numArrFirst[2] == 0)))
        secondFloat = numArrSecond[0] + (numArrSecond[1] / (numArrSecond[2] + (numArrSecond[2] == 0)))

        return [firstFloat, secondFloat]

    #Returns present slider number.
    def sliderNumber(self, base):
        return int(base)

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Converts decimal calculation result back 
    #   to desired floating point number base.
    def outputParse(self, resNum, base):
        #Expresses resulting number as mixed base ten fraction.
        resultDecArr = self.antiFloatAlgorithim(str(resNum), 10)

        #If there is no decimal existing, 
        #   the whole number is converted and displayed. 
        #   Otherwise, more floating point conversions are needed. 
        if (resultDecArr[2] == 0):
            self.calcOutput.delete(0, "end")
            self.calcOutput.insert(0, self.baseConvert.baseConv(resultDecArr[0], base))
        else:
            #Converts whole number to desired base. Fraction is kept 
            #   as base ten fraction for floatAlgorithim to properly parse.
            wholeNum = self.baseConvert.baseConv(resultDecArr[0], base)
            numer = int(resultDecArr[1])
            denom = int(resultDecArr[2])

            result = self.floatAlgorithim(wholeNum, numer, denom, base)

            self.calcOutput.delete(0, "end")
            self.calcOutput.insert(0, result)

        return result

    #Performs adding function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   adding them, then converting them to the desired base.
    def add(self):
        #User input and base fetched.
        floatArr = self.inputParse()
        base = int(self.baseScalar.get())
        
        #Adds the numbers.
        resultDec = floatArr[0] + floatArr[1]
        
        result = self.outputParse(resultDec, base)
        
        #Sets instance variable to calculation result and records action type.
        self.resultNum = result
        self.actionType = 0
    
    #Performs subtracting function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   subtracting them, then converting them to the desired base.
    def subtract(self):
        #User input and base fetched.
        floatArr = self.inputParse()
        base = int(self.baseScalar.get())
        
        #Adds the numbers.
        resultDec = floatArr[0] - floatArr[1]
        
        result = self.outputParse(resultDec, base)
        
        #Result recorded and action type set.
        self.resultNum = result
        self.actionType = 1
    
    #Performs multiplication function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   multiplying them, then converting them to the desired base.
    def multiply(self):
        #User input and base fetched.
        floatArr = self.inputParse()
        base = int(self.baseScalar.get())
        
        #Adds the numbers.
        resultDec = floatArr[0] * floatArr[1]
        
        result = self.outputParse(resultDec, base)

        #Result recorded.
        self.resultNum = result
        self.actionType = 2
    
    #Performs division function of calculator and spits out 
    #   a potential floating point number if division is not even.
    def divide(self):
        #User input and base fetched.
        floatArr = self.inputParse()
        base = int(self.baseScalar.get())
        
        #Adds the numbers.
        resultDec = floatArr[0] / floatArr[1]
        
        result = self.outputParse(resultDec, base)

        self.resultNum = result
        self.actionType = 3
    
    #Converts a whole number and its fraction 
    #   to a floating point of the desired base.
    def floatAlgorithim(self, wholeNum, remainder, divider, base):
        floatStringArr = []
        resultString = str(wholeNum)
        containsAtLeastOneDecimal = False
        
        #Creates a floating point expansion of up to 16 places.
        while (remainder > 0 and len(floatStringArr) < 17):
            remainder *= base
            divResult = remainder // divider
            floatStringArr.append(str(divResult))
            sub = divResult * divider
            remainder -= sub
            containsAtLeastOneDecimal = True

        #Turns each element of the float array to letters 
        #   if the base is larger than 10, 
        #   since decimal has no symbols for numbers greater than nine.
        if base > 10:
            self.baseConvert.toLetters(floatStringArr, base)

        #Adds decimal after whole number if there is a decimal to add.
        resultString += ("." * containsAtLeastOneDecimal) 

        #Uses concatenation to build the final floating point number string.
        for num in floatStringArr:
            resultString += num
        
        return resultString
        
    #Performs the opposite function of the floatAlgorithim, 
    #   converting a floating point number in base 
    #   to a base ten integer with two base ten fractional elements.
    #Returns an array of three elements, 
    #   an integer representing the whole number, 
    #   a numerator representing the floating point number 
    #   of the passed in number, and a denominator. 
    #   All three numbers will be in base ten.
    def antiFloatAlgorithim(self, floatNum, base):
        decimalLoc = 1
        decWasFound = False
        #Finds location of decimal point in number.
        for el in floatNum:
            if el == '.':
                decWasFound = True
                break
            decimalLoc += 1

        #If a decimal wasn't found, the number is converted to base ten 
        #   and returned with numerator and denominator of 0. 
        #Otherwise, further conversion occurs.
        if (decWasFound == False):
            wholeNumDec = self.baseConvert.baseConv(floatNum, base, 2)
            numer = 0
            denom = 0
            return [wholeNumDec, numer, denom]
        else:
            #Whole number and fraction found for number in base.
            wholeNumDec = floatNum[0:(decimalLoc - 1)]
            numer = floatNum[(decimalLoc):]
            denom = "1" + "0" * len(numer)

            wholeNumDec = self.baseConvert.baseConv(wholeNumDec, base, 2)
            numer = self.baseConvert.baseConv(numer, base, 2)
            denom = self.baseConvert.baseConv(denom, base, 2)

            return [wholeNumDec, numer, denom]



def main():
    root = Tk()
    root.title("Base Calculator")
    metric = BaseCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
