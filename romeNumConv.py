#Jesse A. Jones
#Version: 2023-06-01.18

from tkinter import *

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
        self.numE = Entry(self.frameBottom, font = "Ariel 20")
        self.numE.grid(row = 1, column = 0)

        #Converts number to roman numeral when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Roman Numeral", 
            font = "Ariel 60", command = self.romanConverter)
        self.convButtonI.grid(row = 2, column = 0)

        #Roman numeral output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 69", wraplength = 1000)
        self.tOutput.grid(row = 3, column = 0)
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Clears integer input screen.
    def clear(self):
        self.numE.delete(0, "end")

    #Fetches integer input and returns it.
    def properIntGet(self):
        if self.numE.get() == "":
            return 0
        else:
            return int(self.numE.get())

    #Fetches input number, converts it to roman numeral, and displays result.
    def romanConverter(self):
        preConv = self.properIntGet()
        romeNum = self.rome_conv(preConv)
        self.tOutput["text"] = romeNum

    #Takes in an input number and converts 
    #   it to a roman numeral, returning the result.
    def rome_conv(self, decInt):

        #Pointless error checking, have a function do this for you!
        numinit = int(decInt)
        if numinit == 0:
            return ""
        if numinit < 0:
            return ""

        #Take this out of an if statement.
        if numinit > 0:
            #Beefy bois
            numbs = (1000000000000000000000000000000000, 900000000000000000000000000000000, 500000000000000000000000000000000, 400000000000000000000000000000000,
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
                    9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
            romes = ('(==M==)','(==CM==)', '(==D==)', '(==CD==)','(==C==)', '(==XC==)','(==L==)','(==XL==)','(==X==)','(==IX==)','(==V==)','(==IV==)',
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
                    '(|IV|)', 'M','CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
            romenum = []

            """
                THIS CODE BELOW THAT CONVERTS INTS TO ROMAN NUMERALS IS NOT MINE. 
                I FOUND THIS SOMEWHERE ON STACKOVERFLOW A COUPLE YEARS AGO. 
                CREDIT GOES TO THE ORIGIONAL MAKER OF THIS CODE BLOCK.
                I WILL IMPLEMENT A GREEDY ALGORITHIM MYSELF 
                THAT DOES THE SAME THING SOON ENOUGH. 
                FOR NOW, THIS STOLEN CODE WILL HOLD ITS PLACE.  
            """
            for i in range(len(numbs)):
                count = int(numinit / int(numbs[i]))
                romenum.append(romes[i] * count)
                numinit -= int(numbs[i]) * count
            return str(''.join(romenum))
            """
            STOLEN CODE ABOVE /\
            """

def main():
    root = Tk()
    root.title("Roman Numeral Converter (Try not to input a number that is too big.)")
    numb = RomanNumeral(root)
    root.mainloop()

if __name__ == "__main__":
    main()
