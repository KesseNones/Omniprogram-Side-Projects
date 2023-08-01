#Jesse A. Jones
#Version: 2023-08-01.31

from tkinter import *
import dateHandling

#This class takes in a positive integer 
#   and converts it to a roman numeral string.
class RomanNumeral(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button and entry clear button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when called.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        #Clears entry when called.
        self.clearButton = Button(self.frameTop, text = "Clear Entry",
            font = "Ariel 20", command = self.clear)
        self.clearButton.pack(side = LEFT)

        #Holds number input and roman numeral output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Number input field.
        self.message = Label(self.frameBottom, text = "Enter an Integer:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.decNum = Entry(self.frameBottom, font = "Ariel 20")
        self.decNum.grid(row = 1, column = 0)

        #Converts number to roman numeral when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Roman Numeral", 
            font = "Ariel 20", command = self.romanConverter)
        self.convButtonI.grid(row = 2, column = 0)

        #Roman numeral output.
        self.romeOutput = Entry(self.frameBottom, font = "Ariel 20")
        self.romeOutput.grid(row = 3, column = 0)
    
        self.parse = dateHandling.GetDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Clears integer input screen and roman numeral output.
    def clear(self):
        self.decNum.delete(0, "end")
        self.romeOutput.delete(0, "end")

    #Takes in user input and returns a positive integer. 
    #   If the input is wrong, default value 1 is returned.
    def properIntGet(self):
        num = self.parse.getYear(self.decNum.get())
        return (num * [1, -1][num < 0]) + (1 * (num == 0))

    #Fetches input number, converts it to roman numeral, and displays result.
    def romanConverter(self):
        self.romeOutput.delete(0, "end")
        self.romeOutput.insert(0, self.romeConv(self.properIntGet()))

    #Takes in an input number and converts 
    #   it to a roman numeral, returning the result.
    def romeConv(self, decInt):
        #Ensures number isn't bigger than this.
        inputNum = decInt % 4000000000000000000000000000000000 

        romeString = ""

        #Gigantic lists used in determining roman numeral conversion.
        numberList = [1000000000000000000000000000000000, 900000000000000000000000000000000, 500000000000000000000000000000000, 400000000000000000000000000000000,
                100000000000000000000000000000000, 90000000000000000000000000000000, 50000000000000000000000000000000, 40000000000000000000000000000000,
                10000000000000000000000000000000, 9000000000000000000000000000000, 5000000000000000000000000000000, 4000000000000000000000000000000,
                1000000000000000000000000000000, 900000000000000000000000000000, 500000000000000000000000000000, 400000000000000000000000000000,
                100000000000000000000000000000, 90000000000000000000000000000, 50000000000000000000000000000, 40000000000000000000000000000,
                10000000000000000000000000000, 9000000000000000000000000000, 5000000000000000000000000000, 4000000000000000000000000000,
                1000000000000000000000000000, 900000000000000000000000000, 500000000000000000000000000, 400000000000000000000000000,
                100000000000000000000000000, 90000000000000000000000000, 50000000000000000000000000, 40000000000000000000000000,
                10000000000000000000000000, 9000000000000000000000000, 5000000000000000000000000, 4000000000000000000000000,
                1000000000000000000000000, 900000000000000000000000, 500000000000000000000000, 400000000000000000000000, 100000000000000000000000,
                90000000000000000000000, 50000000000000000000000, 40000000000000000000000, 10000000000000000000000,
                9000000000000000000000, 5000000000000000000000, 4000000000000000000000,
                1000000000000000000000, 900000000000000000000, 500000000000000000000, 400000000000000000000,
                100000000000000000000, 90000000000000000000, 50000000000000000000, 40000000000000000000,
                10000000000000000000, 9000000000000000000, 5000000000000000000, 4000000000000000000,
                1000000000000000000, 900000000000000000, 500000000000000000, 400000000000000000,
                100000000000000000, 90000000000000000, 50000000000000000, 40000000000000000,
                10000000000000000, 9000000000000000, 5000000000000000, 4000000000000000,
                1000000000000000, 900000000000000, 500000000000000, 400000000000000, 100000000000000,
                90000000000000, 50000000000000, 40000000000000, 10000000000000, 9000000000000, 5000000000000, 4000000000000,
                1000000000000, 900000000000, 500000000000, 400000000000, 100000000000,
                90000000000, 50000000000, 40000000000, 10000000000, 9000000000, 5000000000, 4000000000,
                1000000000, 900000000, 500000000, 400000000, 100000000, 90000000, 50000000, 40000000, 10000000, 9000000, 5000000, 4000000,
                1000000, 900000,  500000, 400000, 100000,  90000, 50000,  40000, 10000,
                9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romeList = ['(==M==)','(==CM==)', '(==D==)', '(==CD==)','(==C==)', '(==XC==)','(==L==)','(==XL==)','(==X==)','(==IX==)','(==V==)','(==IV==)',
                '(|==M|==)','(|==CM|==)', '(|==D|==)', '(|==CD|==)','(|==C|==)', '(|==XC|==)','(|==L|==)','(|==XL|==)','(|==X|==)','(|==IX|==)','(|==V|==)','(|==IV|==)',
                '(>|||M>|||)','(>|||CM>|||)', '(>|||D>|||)', '(>|||CD>|||)','(>|||C>|||)', '(>|||XC>|||)','(>|||L>|||)','(>|||XL>|||)','(>|||X>|||)','(>|||IX>|||)',
                '(>|||V>|||)','(>|||IV>|||)',
                '(>||M>||)','>(||CM>||)', '(>||D>||)', '(>||CD>||)','(>||C>||)', '(>||XC>||)','(>||L>||)','(>||XL>||)','(>||X>||)','(>||IX>||)','(>||V>||)','(>||IV>||)',
                '(>|M>|)','(>|CM>|)', '(>|D>|)', '(>|CD>|)','(>|C>|)', '(>|XC>|)','(>|L>|)','(>|XL>|)','(>|X>|)','(>|IX>|)','(>|V>|)','(>|IV>|)',
                '(>M>)','(>CM>)', '(>D>)', '(>CD>)','(>C>)', '(>XC>)','(>L>)','(>XL>)','(>X>)','(>IX>)','(>V>)','(>IV>)',
                '(|>M|>)','(|>CM|>)', '(|>D|>)', '(|>CD|>)','(|>C|>)', '(|>XC|>)','(|>L|>)','(|>XL|>)','(|>X|>)','(|>IX|>)','(|>V|>)','(|>IV|>)',
                '(|||M|||)','(|||CM|||)', '(|||D|||)', '(|||CD|||)','(|||C|||)', '(|||XC|||)','(|||L|||)','(|||XL|||)','(|||X|||)','(|||IX|||)','(|||V|||)','(|||IV|||)',
                '(||M||)','(||CM||)', '(||D||)', '(||CD||)','(||C||)', '(||XC||)','(||L||)','(||XL||)','(||X||)','(||IX||)','(||V||)','(||IV||)',
                '(|M|)', '(|CM|)', '(|D|)', '(|CD|)','(|C|)', '(|XC|)','(|L|)','(|XL|)','(|X|)','(|IX|)','(|V|)',
                '(|IV|)', 'M','CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']

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
    root.title("Roman Numeral Converter (Try not to input a number that is too big.)")
    numb = RomanNumeral(root)
    root.mainloop()

if __name__ == "__main__":
    main()
