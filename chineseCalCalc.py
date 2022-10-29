from tkinter import *
import math
from math import log

class ChineseCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 55")
        self.yearE.grid(row = 1, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Convert to Chinese Calendar Year", 
            font = "Ariel 60", command = self.yearToCal)
        self.convButtonI.grid(row = 2, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 60", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
    def quitButtonAction(self):
        self.window.destroy()

    def yearToCal(self):
        date = self.chiCal()
        self.tOutput["text"] = date 

    def yearGet(self):
        if self.yearE.get() == "":
            return 0
        else:
            return int(self.yearE.get())

    def chiCal(self):
        baseCycleNum = 78
        year = self.yearGet()
        if year >= 1984:
            cycleNum = ((year - 1984) % 60) + 1
            cyc = baseCycleNum + ((year - 1984) // 60)
        if year < 1984:
            cycleNum = (((year - 1984) + 60) % 60) + 1
            cyc = baseCycleNum + ((year - 1984) // 60)
        zodNum = ((cycleNum - 1) % 12)
        elemNum = ((cycleNum - 1) // 12)
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
        calString = "Cycle: " + str(cyc) + ", Year: " + str(cycleNum) + ", " + yangYin + " " + el + "-" + amnimal
        return calString
        

def main():
    root = Tk()
    root.title("Chinese Calendar Year Calclator")
    temp = ChineseCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
