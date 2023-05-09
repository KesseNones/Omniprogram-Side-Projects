#Jesse A. Jones
#Version: 2023-05-09.11

from tkinter import *
import math
from math import log

#This class takes in an input year in the API 
#   and converts it to a year in the Chinese Calendar.

class ChineseCalCalc(object):

    #Sets up GUI
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds input year and convert button.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Creates year input zone.
        self.message = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.yearE = Entry(self.frameBottom, font = "Ariel 20")
        self.yearE.grid(row = 1, column = 0)

        #Button that causes conversion to chinese calendar year.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Chinese Calendar Year", 
            font = "Ariel 20", command = self.yearToCal)
        self.convButtonI.grid(row = 2, column = 0)

        #Output text.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls functions to convert gregorian year to chinese year.
    def yearToCal(self):
        date = self.chiCal()
        self.tOutput["text"] = date 

    #Fetches input year.
    def yearGet(self):
        if self.yearE.get() == "":
            return 0
        else:
            return int(self.yearE.get())

    #Calculates the chinese year based on what year was given.
    def chiCal(self):
        baseCycleNum = 78
        year = self.yearGet()
        
        #Calculates cycle and cycle number based 
        #   on if year is >= 1984 or not.
        if year >= 1984:
            cycleNum = ((year - 1984) % 60) + 1
            cyc = baseCycleNum + ((year - 1984) // 60)
        else:
            cycleNum = (((year - 1984) + 60) % 60) + 1
            cyc = baseCycleNum + ((year - 1984) // 60)
        
        #Calculates zodiac number and element number.
        zodNum = ((cycleNum - 1) % 12)
        elemNum = ((cycleNum - 1) // 12)
        
        #Calculates element name for case Rat.
        if zodNum == 0:
            amnimal = "Rat"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Wood"
            if elemNum == 1:
                el = "Fire"
            if elemNum == 2:
                el = "Earth"
            if elemNum == 3:
                el = "Metal"
            if elemNum == 4:
                el = "Water"

        #Calculates element name for case Ox.
        if zodNum == 1:
            amnimal = "Ox"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Wood"
            if elemNum == 1:
                el = "Fire"
            if elemNum == 2:
                el = "Earth"
            if elemNum == 3:
                el = "Metal"
            if elemNum == 4:
                el = "Water"
        
        #Calculates element name for case Tiger.
        if zodNum == 2:
            amnimal = "Tiger"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Fire"
            if elemNum == 1:
                el = "Earth"
            if elemNum == 2:
                el = "Metal"
            if elemNum == 3:
                el = "Water"
            if elemNum == 4:
                el = "Wood"

        #Calculates element name for case Rabbit.
        if zodNum == 3:
            amnimal = "Rabbit"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Fire"
            if elemNum == 1:
                el = "Earth"
            if elemNum == 2:
                el = "Metal"
            if elemNum == 3:
                el = "Water"
            if elemNum == 4:
                el = "Wood"

        #Calculates element name for case Dragon.
        if zodNum == 4:
            amnimal = "Dragon"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Earth"
            if elemNum == 1:
                el = "Metal"
            if elemNum == 2:
                el = "Water"
            if elemNum == 3:
                el = "Wood"
            if elemNum == 4:
                el = "Fire"

        #Calculates element name for case Snake.
        if zodNum == 5:
            amnimal = "Snake"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Earth"
            if elemNum == 1:
                el = "Metal"
            if elemNum == 2:
                el = "Water"
            if elemNum == 3:
                el = "Wood"
            if elemNum == 4:
                el = "Fire"

        #Calculates element name for case Horse.
        if zodNum == 6:
            amnimal = "Horse"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Metal"
            if elemNum == 1:
                el = "Water"
            if elemNum == 2:
                el = "Wood"
            if elemNum == 3:
                el = "Fire"
            if elemNum == 4:
                el = "Earth"

        #Calculates element name for case Goat.
        if zodNum == 7:
            amnimal = "Goat"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Metal"
            if elemNum == 1:
                el = "Water"
            if elemNum == 2:
                el = "Wood"
            if elemNum == 3:
                el = "Fire"
            if elemNum == 4:
                el = "Earth"

        #Calculates element name for case Monkey.
        if zodNum == 8:
            amnimal = "Monkey"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Water"
            if elemNum == 1:
                el = "Wood"
            if elemNum == 2:
                el = "Fire"
            if elemNum == 3:
                el = "Earth"
            if elemNum == 4:
                el = "Metal"

        #Calculates element name for case Rooster.
        if zodNum == 9:
            amnimal = "Rooster"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Water"
            if elemNum == 1:
                el = "Wood"
            if elemNum == 2:
                el = "Fire"
            if elemNum == 3:
                el = "Earth"
            if elemNum == 4:
                el = "Metal"

        #Calculates element name for case Dog.
        if zodNum == 10:
            amnimal = "Dog"
            yangYin = "Yang"
            if elemNum == 0:
                el = "Wood"
            if elemNum == 1:
                el = "Fire"
            if elemNum == 2:
                el = "Earth"
            if elemNum == 3:
                el = "Metal"
            if elemNum == 4:
                el = "Water"

        #Calculates element name for case Pig.
        if zodNum == 11:
            amnimal = "Pig"
            yangYin = "Yin"
            if elemNum == 0:
                el = "Wood"
            if elemNum == 1:
                el = "Fire"
            if elemNum == 2:
                el = "Earth"
            if elemNum == 3:
                el = "Metal"
            if elemNum == 4:
                el = "Water"

        #Builds final string and returns it.
        calString = "Cycle: " + str(cyc) + ", Year: " + str(cycleNum) + ", " + yangYin + " " + el + "-" + amnimal
        return calString
        

def main():
    root = Tk()
    root.title("Chinese Calendar Year Calclator")
    temp = ChineseCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
