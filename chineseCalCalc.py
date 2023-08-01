#Jesse A. Jones
#Version: 2023-08-01.28

from tkinter import *
import math
import dateHandling

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
    
        self.parse = dateHandling.GetDate()

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls functions to convert gregorian year to chinese year.
    def yearToCal(self):
        self.tOutput["text"] = self.chiCal() 

    #Calculates the chinese year based on what year was given.
    def chiCal(self):
        baseCycleNum = 78
        year = self.parse.getYear(self.yearE.get())
        
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
        
        #Useful arrays necessary for calculations.
        zodNameArr = ["Rat", "Ox", "Tiger",
                    "Rabbit", "Dragon", "Snake",
                    "Horse", "Goat", "Monkey", 
                    "Rooster", "Dog", "Pig"]
        yangYinArr = ["Yang", "Yin"]
        elementNameArr = ["Wood", "Fire", "Earth", "Metal", "Water"]

        #Finds zodiac animal.
        animal = zodNameArr[zodNum]
        
        #Finds yin or yang.
        yangYin = yangYinArr[zodNum % 2]
        
        #Finds element name.
        el = elementNameArr[(elemNum + (zodNum // 2)) % 5]

        #Builds final string and returns it.
        calString = "Cycle: " + str(cyc) + ", Year: " + str(cycleNum) + ", " + yangYin + " " + el + "-" + animal
        return calString
        
def main():
    root = Tk()
    root.title("Chinese Calendar Year Calclator")
    temp = ChineseCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
