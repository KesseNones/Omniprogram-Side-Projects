#Jesse A. Jones
#Version: 2023-05-23.07

from tkinter import *
import dateHandling
from math import log10

#This class takes in an input number and displays the number 
#   in scientific notation as well as the name of the number.
class BigNumbUnderstander(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button and clear entry button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        #Clears number input field when pressed.
        self.clearButton = Button(self.frameTop, text = "Clear Entry",
            font = "Ariel 20", command = self.clear)
        self.clearButton.pack(side = LEFT)

        #Bottom frame holds number input field, 
        #   conversion button, and number output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Number input field.
        self.message = Label(self.frameBottom, text = "Enter a Number:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.num = Entry(self.frameBottom, font = "Ariel 20")
        self.num.grid(row = 1, column = 0)

        #Converts input number to something readable when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Understandibleness", 
            font = "Ariel 20", command = self.numbConverter)
        self.convButtonI.grid(row = 2, column = 0)

        #Outputs number decimal.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        #Outputs number name.
        self.tOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutputII.grid(row = 4, column = 0)

        #Outputs scientific notation button.
        self.tOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutputIII.grid(row = 5, column = 0)

        self.numGet = dateHandling.GetDate()
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Clears number input field.
    def clear(self):
        self.num.delete(0, "end")

    def clearOutput(self):
        self.tOutput["text"] = ""
        self.tOutputII["text"] = ""
        self.tOutputIII["text"] = ""

    #Calls functions to convert input number to something 
    #   with a name and scientific notation to a limit.
    def numbConverter(self):
        
        #Derives input number and converts it to sci notation components.
        inputNum = self.numGet.getGeneral(self.num.get()) 
        
        if inputNum != float("inf"):
            sciNumArr = self.numToSciNot(inputNum)
            
            self.clearOutput()

            #Displays reults of function calls.
            self.tOutput["text"] = str(round(sciNumArr[0] * (10 ** (sciNumArr[1] % 3)), 3) )
            self.tOutputII["text"] = self.expToName(sciNumArr[1])
            self.tOutputIII["text"] = f"{sciNumArr[0]} X 10 ^ {sciNumArr[1]}"
            self.frameBottom.update()

    #Takes an input number and breaks it down 
    #   into its decimal compoenent and exponent.
    def numToSciNot(self, num):
        #Parses input number to see if it's 0.
        if num == 0:
            return [0.0, 0]
        
        logNum = log10(num)

        exp = int(logNum)
        decNum = round((10 ** (logNum - exp)), 3)

        return [decNum, exp]     

    #Takes in an exponent and returns the name of the thousand power it's in.
    def expToName(self, exp):
        #Holds all exponent thousand multiple names.
        nameList = ["", "thousand", "million", "billion", 
                    "trillion", "quadrillion", "quintillion", 
                    "sextillion", "septillion", "octillion", 
                    "nonillion", "decillion", "undecillion", 
                    "duodecillion", "tredecillion", "quattuordecillion", 
                    "quindecillion", "sexdecillion", "septendecillion",
                    "octodecillion", "novemdecillion", "vigintillion",
                    "unvigintillion", "duovigintillion", "tresvigintillion",
                    "quattuorvigintillion", "quinvigintillion", "sesvigintillion"
                    "septemvigintillion", "octovigintillion", "novemvigintillion",
                    "trigintillion", "untrigintillion", "duotrigintillion",
                    "trestrigintillion", "quattuortrigintillion", "quintrigintillion",
                    "sestrigintillion", "septentrigintillion", "octotrigintillion", 
                    "noventrigintillion", "quadragintillion", "unquadragintillion", 
                    "duoquadragintillion", "tresquadragintillion", "quattuorquadragintillion", 
                    "quinquequadragintillion", "sesquadragintillion", "septenquadragintillion",
                    "octoquadragintillion", "novemquadragintillion", "quinquagintillion",
                    "unquinquagintillion", "duoquinquagintillion", "trequinquagintillion",
                    "quattuorquinquagintillion", "quinquenquinquagintillion", "sesquinquagintillion",
                    "septenquinquagintillion", "octoquinquagintillion", "novemquinquagintillion",
                    "sexagintillion", "unsexagintillion", "duosexagintillion",
                    "tresexagintillion", "quattuorsexagintillion", "quinquesexagintillion",
                    "sessexagintillion", "septensexagintillion", "octosexagintillion",
                    "novemsexagintillion", "septuagintillion", "unseptuagintillion",
                    "duoseptuagintillion", "treseptuagintillion", "quattuorseptuagintillion", 
                    "quinqueseptuagintillion", "sesseptuagintillion", "septenseptuagintillion", 
                    "octoseptuagintillion", "novemseptuagintillion", "octogintillion", 
                    "unoctogintillion", "duooctogintillion", "tresoctogintillion", 
                    "quattuoroctogintillion", "quinqueoctogintillion", "sesoctogintillion", 
                    "septenoctogintillion", "octumoctogintillion", "novemoctogintillion", 
                    "nonagintillion", "unonagintillion", "duononagintillion", 
                    "tresnonagintillion", "quattuornonagintillion", "quinquenonagintillion", 
                    "sesnonagintillion", "septennonagintillion", "octononagintillion", 
                    "novemnonagintillion", "centillion", "uncentillion", "duocentillion"]

        index = abs(exp) // 3

        return nameList[index]

def main():
    root = Tk()
    root.title("Big Number Understander")
    numb = BigNumbUnderstander(root)
    root.mainloop()

if __name__ == "__main__":
    main()
