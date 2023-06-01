#Jesse A. Jones
#Version: 2023-06-01.26

import datetime
from tkinter import *

#This clock displays the date and time using roman numerals.
class RomeNumTime(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("600x200")

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when called.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds date and time output fields.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Date output field.
        self.date = Label(self.frameBottom, text = "", font = "Ariel 40", anchor = "w")
        self.date.grid(row = 0, column = 0)
        
        #Time output field.
        self.time = Label(self.frameBottom, text = "", font = "Ariel 40")
        self.time.grid(row = 1, column = 0)
    
        #Starts recursive time update loop.
        self.timeUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Finds roman numeral time strings and displays result.
    def timeUpdate(self):
        timeString = self.timeConv()
        self.date["text"] = timeString[0]
        self.time["text"] = timeString[1]
        self.date.after(1, self.timeUpdate)

    #Gets current time using datetime and converts each number 
    #   to roman numerals, returning the date 
    #   and time strings constructed as such.
    def timeConv(self):
        #Grabs current time and date, and saves it in list.
        local = datetime.datetime.now()
        dateTimeArr = [local.year, local.month, local.day, local.hour, local.minute, local.second]

        romeTimeArr = []
        
        #Converts each element of the dateTimeArr to roman numerals.
        for el in dateTimeArr:
            romeTimeArr.append(self.romeConv(el))

        #Builds date and time strings, returning them.
        dateString = str(romeTimeArr[0]) + "-" + str(romeTimeArr[1]) + "-" + str(romeTimeArr[2])
        timeString = str(romeTimeArr[3]) + ":" + str(romeTimeArr[4]) + ":" + str(romeTimeArr[5])
        return [dateString, timeString]

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
    root.title("Roman Numeral Time")
    metric = RomeNumTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
