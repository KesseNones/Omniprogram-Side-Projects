#Jesse A. Jones
#Version: 2022-11-02.2

import datetime
import time
from tkinter import *

class CenTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.date = Label(self.frameBottom, text = "test", font = "Times 75", anchor = "w")
        self.date.grid(row = 0, column = 0)
        
        self.time = Label(self.frameBottom, text = "", font = "Times 75")
        self.time.grid(row = 1, column = 0)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        timeString = self.timeConv()
        self.date["text"] = timeString[0]
        self.time["text"] = timeString[1]
        self.date.after(1, self.timeUpdate)

    def timeConv(self):
        retArr = []
        local = datetime.datetime.now()
        dateTimeArr = [local.year, local.month, local.day, local.hour, local.minute, local.second]
        romeTimeArr = []
        for el in dateTimeArr:
            romeTimeArr.append(self.rome_conv(el))
        dateString = str(romeTimeArr[0]) + "-" + str(romeTimeArr[1]) + "-" + str(romeTimeArr[2])
        timeString = str(romeTimeArr[3]) + ":" + str(romeTimeArr[4]) + ":" + str(romeTimeArr[5])
        retArr.append(dateString)
        retArr.append(timeString)
        return retArr

    def rome_conv(self, decInt):
        #This function takes in an integer and returns 
        #   a string representing its equivalent roman numeral.

        numinit = int(decInt)
        if numinit == 0:
            return ""
        if numinit < 0:
            return ""
        if numinit > 0:
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
    root.title("Roman Numeral Time")
    metric = CenTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
