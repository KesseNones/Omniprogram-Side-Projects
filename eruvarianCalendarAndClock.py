#Jesse A. Jones
#Version: 2023-05-19.09

import time
from tkinter import *
import baseConvertClass

#This class displays the current date in the Eru'varian calendar 
#   and shows the Eru'varian time. The calendar consists 
#   of 12 lunar cycles each containing 30 Eru'varian days and 5 six day weeks.
#   An Eru'varian year is about 1.009 Earth years and an Eru'varian day 
#   is 2000 seconds longer than an Earth day.
class EruCal(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program if clicked.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time and date outputs.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays time.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.message.grid(row = 0, column = 0)
        
        #Displays date
        self.messageII = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.messageII.grid(row = 1, column = 0)

        #Displays Sub-Age, a period lasting 20736 (10000 in base 12) Eru'varian years.
        #   This is hard coded because we have millennia until the sub age turns over 
        #   and I doupt anyone will be running this program at that time. And if they are, joke's on them! 
        self.messageIII = Label(self.frameBottom, text = "Sub-Age: 281171", font = "Ariel 50", anchor = "w")
        self.messageIII.grid(row = 2, column = 0)
    
        #Displays the age itself. This age won't change until Ragnerok trillions 
        #   of years from no so we're good to just hard code the value for this.
        self.cOutputIII = Label(self.frameBottom, text = "Age of Balance", 
            font = "Ariel 50")
        self.cOutputIII.grid(row = 3, column = 0)

        #Starts the recursive time update loop.
        self.timeUpdate()

    #Quits program
    def quitButtonAction(self):
        self.window.destroy()

    #Finds time and date in Eru'varian calendar and updates stuff as such.
    def timeUpdate(self):
        #88400
        timeArr = self.eruConv(time.time())
        self.message["text"] = timeArr[0]
        self.messageII["text"] = timeArr[1]
        self.message.after(1, self.timeUpdate)

    #Calculates Eru'varian date and time and returns 
    #   and updates the appropriate fields.
    def eruConv(self, unix):
        #Calculates Eru'varian years elapsed and current year.
        eruYearsElapsed = unix // 31824000
        eruYear = 5376 + eruYearsElapsed

        #Calculates Eru'varian date based on seconds in current Eru'varian year.
        secondsOfCurrentYear = unix % 31824000
        lunarCycle = secondsOfCurrentYear // 2652000
        secondsOfCurrentLunarCycle = secondsOfCurrentYear % 2652000
        eruDay = secondsOfCurrentLunarCycle // 88400
        eruWeekdayNum = int(eruDay) % 6
        weekArr = ["Torfung", "Solfung", "Varfung", "Melfung", "Orivfung", "T'rarfung"]
        eruWeekday =  weekArr[eruWeekdayNum]

        #Fractions used in calculating Eru'varian time.
        eruSecTotal = unix % 88400
        twelfth = 88400 / 12
        onefortyfourth = 88400 / 144
        oneseventeentwentyeigth = 88400 / 1728
        onetwentyK = 88400 / 20736
        onetwofiftyK = 88400 / 248832

        #Calculates places of Eru'varian time.
        twelfths = eruSecTotal // twelfth
        reducedEruSecI = eruSecTotal % twelfth
        onefortyfourths = reducedEruSecI // onefortyfourth
        reducedEruSecII = reducedEruSecI % onefortyfourth
        oneseventeentwentyeigths = reducedEruSecII // oneseventeentwentyeigth
        reducedEruSecIII = reducedEruSecII % oneseventeentwentyeigth
        onetwentyKs = reducedEruSecIII // onetwentyK
        reducedEruSecIV = reducedEruSecIII % onetwentyK
        onetwofiftyKs = reducedEruSecIV // onetwofiftyK

        #Converts Eru'varian time to base 12.
        base = baseConvertClass.BaseConvert()
        firstPlace = base.baseConv(int(twelfths), 12)
        secondPlace = base.baseConv(int(onefortyfourths), 12)
        thirdPlace = base.baseConv(int(oneseventeentwentyeigths), 12)
        fourthPlace = base.baseConv(int(onetwentyKs), 12)
        fifthPlace = base.baseConv(int(onetwofiftyKs), 12)

        #Converts date numbers to base 12.
        trueEruYear = base.baseConv(int(eruYear), 12)
        trueEruLunarCycle = base.baseConv(int(lunarCycle), 12)
        trueEruDay = base.baseConv(int(eruDay), 12)

        #Constructs time strings and returns them.
        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        otherTimeString = trueEruYear + "-" + trueEruLunarCycle + "-" + trueEruDay.zfill(2) + ", " + eruWeekday
        return [timeString, otherTimeString]

def main():
    root = Tk()
    root.title("Eru'varian Clock and Calendar")
    metric = EruCal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
