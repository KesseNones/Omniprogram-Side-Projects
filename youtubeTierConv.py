#Jesse A. Jones
#Version: 2023-06-13.12

from tkinter import *
from math import log10
from math import log
from tkinter import messagebox

#This class converts a subscriber count to a youtube tier and vice versa.
class YoutubeTierConv(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds sub and tier input fields, conversion buttons, 
        #   and converted outputs.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        FONT = "Ariel 20"

        #Subscriber count input field.
        self.messageI = Label(self.frameBottom, text = "Enter Sub Count:", font = FONT, anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.sI = Entry(self.frameBottom, font = FONT)
        self.sI.grid(row = 0, column = 1)

        #Converts subscriber count to tier when pressed.
        self.tierButton = Button(self.frameBottom, text = "Convert to Tier", 
            font = FONT, command = self.subToTier)
        self.tierButton.grid(row = 1, column = 0)

        #Youtube tier output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.tOutput.grid(row = 1, column = 1)

        #Displays classic tier.
        self.tOutputII = Label(self.frameBottom, text = "", 
            font = FONT)
        self.tOutputII.grid(row = 2, column = 1)

        #Tier input field.
        self.messageII = Label(self.frameBottom, text = "Enter Tier:", font = FONT, anchor = "w")
        self.messageII.grid(row = 4, column = 0)
        self.tier = Entry(self.frameBottom, font = FONT)
        self.tier.grid(row = 4, column = 1)

        #Converts tier to subscriber count.
        self.cButton = Button(self.frameBottom, text = "Convert to Sub Count", 
            font = FONT, command = self.tierToSub)
        self.cButton.grid(row = 5, column = 0)

        #Displays subscriber count based on tier.
        self.sOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.sOutput.grid(row = 5, column = 1)
        
        #Holds named number of subscribers.
        self.sOutputII = Label(self.frameBottom, text = "", 
            font = FONT)
        self.sOutputII.grid(row = 6, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Parses input subscriber count.
    def subCount(self):
        subInput = self.sI.get()
        if subInput != "" and float(subInput) >= 0 and float(subInput) < 1.797693e+308:
            return float(subInput)
        else:
            return 0.0

    #Parses input tier.
    def tierGet(self):
        tierInput = self.tier.get()
        if tierInput != "" and float(tierInput) >= 0 and float(tierInput) <= 153.562:
            return float(tierInput)
        else:
            return 0.0

    #Converts subscriber count to tier.
    def subToTier(self):
        subs = self.subCount()
        tier = None

        #Accounts for tier 0 case.
        if 0 <= subs < 1000:
            tier = subs / 1000

        #Tier 1 and beyond case.
        else:
            tier = log(subs, 100) - 0.5
            tier = round(tier, 9)

        #Displays resulting tier.
        self.tOutput["text"] = f"Tier: {tier}"
        self.tOutputII["text"] = f"Classic Tier: {self.romeConv(int(tier))}"

    #Converts tier number to subscriber count.
    def tierToSub(self):
        tier = self.tierGet()

        #Tier 0 case.
        if 0 <= tier < 1:
            subs = tier * 1000
        #Tier 1 and beyond case.
        else:
            subs = (100 ** tier) * 10

        #Calculates big number display for subscriber count.
        sciNotation = self.numToSciNot(subs)

        self.sOutput["text"] = f"{sciNotation[0] * (10 ** (sciNotation[1] % 3))} {self.expToName(sciNotation[1])} Subscribers"
        self.sOutputII["text"] = f"({round(subs, 3)})"

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

    #Takes in an input number and converts 
    #   it to a roman numeral, returning the result.
    def romeConv(self, decInt):
        if decInt == 0:
            return "Zero"
        #Ensures number isn't bigger than this.
        inputNum = decInt % 4000 

        romeString = ""

        #Gigantic lists used in determining roman numeral conversion.
        numberList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romeList = ['M','CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']

        index = 0
        numLeft = inputNum
        goesInTimes = 0

        #Iterates through number list and greedily builds 
        #   roman numeral string based on what goes in.
        for el in numberList:
            if index % 2 == 0:
                goesInTimes = numLeft // el
                numLeft -= goesInTimes * el

                while goesInTimes > 0:
                    romeString += romeList[index]
                    goesInTimes -= 1
            else:
                if numLeft // el == 1:
                    romeString += romeList[index]
                    numLeft -= el
            index += 1

        return romeString

def main():
    root = Tk()
    root.title("Youtube Tier Converter")
    star = YoutubeTierConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
