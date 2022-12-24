#Jesse A. Jones
#Version: 2022-12-24.4

from tkinter import *
import baseConvertClass

#This class contains fields and methods necessary for a calculator 
#   to calculate the four basic calculator operations for bases 2 through 36.
#FLOATING POINTS ARE A WORK IN PROGRESS AND ONLY WORK AS A DIVISION RESULT DISPLAY!
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
        cmdArr = [self.add(), self.subtract(), self.multiply(), self.divide()]
        cmdArr[self.actionType]

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
    
    #Returns present slider number.
    def sliderNumber(self, base):
        return int(base)

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Performs adding function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   adding them, then converting them to the desired base.
    def add(self):
        #Input base and fields fetched.
        base = int(self.baseScalar.get())
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        #Input fields converted to base ten.
        firstDec = self.baseConvert.baseConv(first, base, 2)
        secondDec = self.baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec + secondDec
        
        #Converts result back to input base.
        result = self.baseConvert.baseConv(resultDec, base)
        
        #Displays result.
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)
        
        #Sets instance variable to calculation result and records action type.
        self.resultNum = result
        self.actionType = 0
    
    #Performs subtracting function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   subtracting them, then converting them to the desired base.
    def subtract(self):
        #Input base and fields fetched.
        base = int(self.baseScalar.get())
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        #Input fields converted to base ten.
        firstDec = self.baseConvert.baseConv(first, base, 2)
        secondDec = self.baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec - secondDec
        
        #Result converted back to input base and displayed to user.
        result = self.baseConvert.baseConv(resultDec, base)
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)
        
        #Result recorded.
        self.resultNum = result
        self.actionType = 1
    
    #Performs multiplication function of calculator in a lazy manner, 
    #   by converting both inputs to base ten, 
    #   multiplying them, then converting them to the desired base.
    def multiply(self):
        #Inputs fetched.
        base = int(self.baseScalar.get())
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        #Conversion of input to base ten.
        firstDec = self.baseConvert.baseConv(first, base, 2)
        secondDec = self.baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec * secondDec
        
        #Conversion of result back to original base 
        #   and result displayed to user.
        result = self.baseConvert.baseConv(resultDec, base)
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)

        #Result recorded.
        self.resultNum = result
        self.actionType = 2
    
    #Performs division function of calculator and spits out 
    #   a potential floating point number if division is not even.
    def divide(self):
        #Input fetch.
        base = int(self.baseScalar.get())
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        #Base ten conversion.
        firstDec = self.baseConvert.baseConv(first, base, 2)
        secondDec = self.baseConvert.baseConv(second, base, 2)
        
        #Makes sure no division by zero occurs.
        if secondDec == 0:
            return
        
        #Whole number component of division.
        resultIntDec = firstDec // secondDec
        
        #Remainder.
        rem = firstDec % secondDec
        
        #Components converted to desired base.
        resultWhole = self.baseConvert.baseConv(resultIntDec, base)
        resultNumerator = self.baseConvert.baseConv(rem, base)
        resultDenominator = self.baseConvert.baseConv(secondDec, base)
        
        #If the result is an integer, the resulting number is set as such, 
        #   otherwise a floating point algorithim needs to be employed.
        if rem == 0:
            resultString = resultWhole
        else:
            resultString = self.floatAlgorithim(resultWhole, rem, secondDec, base)

        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, resultString)
    
    #Converts a whole number and its fraction 
    #   to a floating point of the desired base.
    def floatAlgorithim(self, wholeNum, remainder, divider, base):
        floatStringArr = []
        resultString = str(wholeNum) + "."
        
        #Creates a floating point expansion of up to 16 places.
        while (remainder > 0 and len(floatStringArr) < 17):
            remainder *= base
            divResult = remainder // divider
            floatStringArr.append(str(divResult))
            sub = divResult * divider
            remainder -= sub

        #Turns each element of the float array to letters 
        #   if the base is larger than 10, 
        #   since decimal has no symbols for numbers greater than nine.
        if base > 10:
            self.baseConvert.toLetters(floatStringArr, base)

        #Uses concatenation to build the final floating point number string.
        for num in floatStringArr:
            resultString += num
        
        return resultString
        
def main():
    root = Tk()
    root.title("Base Calculator")
    metric = BaseCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
