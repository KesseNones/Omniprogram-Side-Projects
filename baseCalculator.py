from tkinter import *
import math
import baseConvertClass

class BaseCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column= 0)
        
        self.clearButton = Button(self.frameTop, text = "Clear",
            font = "Ariel 20", command = self.clear)
        self.clearButton.grid(row = 0, column= 1)
        
        self.repeatButton = Button(self.frameTop, text = "Repeat Calculation",
            font = "Ariel 20", command = self.repeat)
        self.repeatButton.grid(row = 0, column= 2)

        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 1, column = 0)

        self.messageI = Label(self.frameBottom, text = "First Input:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.first = Entry(self.frameBottom, font = "Times 69")
        self.first.grid(row = 1, column = 0)

        self.messageII = Label(self.frameBottom, text = "Second Input:", font = "Ariel 55", anchor = "w")
        self.messageII.grid(row = 3, column = 0)

        self.second = Entry(self.frameBottom, font = "Times 69")
        self.second.grid(row = 4, column = 0)

        self.baseScalar = Scale(self.frameBottom, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 400, 
            label = "Base:", font = "Times 55", command = self.sliderNumber)
        self.baseScalar.grid(row = 5, column = 0)

        self.frameRockBottom = Frame(self.window)
        self.frameRockBottom.grid(row = 1, column = 1)

        self.addButton = Button(self.frameRockBottom, text = "Add", 
            font = "Ariel 55", command = self.add)
        self.addButton.grid(row = 0, column = 0)
        
        self.subtractButton = Button(self.frameRockBottom, text = "Sub", 
            font = "Ariel 55", command = self.subtract)
        self.subtractButton.grid(row = 0, column = 1)
        
        self.multiplyButton = Button(self.frameRockBottom, text = "Mult", 
            font = "Ariel 55", command = self.multiply)
        self.multiplyButton.grid(row = 1, column = 0)
        
        self.divideButton = Button(self.frameRockBottom, text = "Div", 
            font = "Ariel 55", command = self.divide)
        self.divideButton.grid(row = 1, column = 1)

        self.calcOutput = Entry(self.frameBottom, font = "Ariel 55")
        self.calcOutput.grid(row = 7, column = 0)
        
        self.resultNum = ""
        self.actionType = -1

    def repeat(self):
        self.first.delete(0, "end")
        self.first.insert(0, self.resultNum)
        if (self.actionType == 0):
            self.add()
        elif (self.actionType == 1):
            self.subtract()
        elif (self.actionType == 2):
            self.multiply()
        elif(self.actionType == 3):
            pass
        else:
            pass

    def clear(self):
        self.resultNum = ""
        self.actionType = 0
        self.first.delete(0, "end")
        self.second.delete(0, "end")
        self.calcOutput.delete(0, "end")

    def inputFetch(self, input):
        if input == "":
            return "0"
        else:
            return input
    
    def sliderNumber(self, base):
        return int(base)

    def quitButtonAction(self):
        self.window.destroy()

    def add(self):
        baseConvert = baseConvertClass.BaseConvert()
        base = int(self.baseScalar.get())
        
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        firstDec = baseConvert.baseConv(first, base, 2)
        secondDec = baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec + secondDec
        
        result = baseConvert.baseConv(resultDec, base)
        
        # self.first.delete(0, "end")
        # self.first.insert(0, self.resultNum)
        
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)
        
        self.resultNum = result
        self.actionType = 0
    
    def subtract(self):
        baseConvert = baseConvertClass.BaseConvert()
        base = int(self.baseScalar.get())
        
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        firstDec = baseConvert.baseConv(first, base, 2)
        secondDec = baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec - secondDec
        
        result = baseConvert.baseConv(resultDec, base)
        
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)
        
        self.resultNum = result
        self.actionType = 1
    
    def multiply(self):
        baseConvert = baseConvertClass.BaseConvert()
        base = int(self.baseScalar.get())
        
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        firstDec = baseConvert.baseConv(first, base, 2)
        secondDec = baseConvert.baseConv(second, base, 2)
        
        resultDec = firstDec * secondDec
        
        result = baseConvert.baseConv(resultDec, base)
        
        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, result)

        self.resultNum = result
        self.actionType = 2
    
    def divide(self):
        baseConvert = baseConvertClass.BaseConvert()
        base = int(self.baseScalar.get())
        
        first = self.inputFetch(self.first.get())
        second = self.inputFetch(self.second.get())
        
        firstDec = baseConvert.baseConv(first, base, 2)
        secondDec = baseConvert.baseConv(second, base, 2)
        
        if secondDec == 0:
            self.calcOutput["text"] = "Error! Cannot divide by zero!"
            return
        
        resultIntDec = firstDec // secondDec
        
        rem = firstDec % secondDec
        
        resultWhole = baseConvert.baseConv(resultIntDec, base)
        resultNumerator = baseConvert.baseConv(rem, base)
        resultDenominator = baseConvert.baseConv(secondDec, base)
        
        if rem == 0:
            resultString = resultWhole
        else:
            #resultString = resultWhole + " and " + resultNumerator + "/" + resultDenominator
            resultString = self.floatAlgorithim(resultWhole, rem, secondDec, base)

        self.calcOutput.delete(0, "end")
        self.calcOutput.insert(0, resultString)
    
    def floatAlgorithim(self, wholeNum, remainder, divider, base):
        toLetters = baseConvertClass.BaseConvert()
        floatStringArr = []
        resultString = str(wholeNum) + "."
        while (remainder > 0 and len(floatStringArr) < 17):
            remainder *= base
            divResult = remainder // divider
            floatStringArr.append(str(divResult))
            sub = divResult * divider
            remainder -= sub
        if base > 10:
            toLetters.toLetters(floatStringArr, base)
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
