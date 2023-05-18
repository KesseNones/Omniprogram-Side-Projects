#Jesse A. Jones
#Version: 2023-05-18.92

import time
from tkinter import *
import baseConvertClass

#This class displays the Eru'varian clock used by the Eru'varians. 
#   This clock is in base 12 and counts 12 hours in an Eru'varian day 
#   which is about 2000 seconds longer than our days. 
#   Eru'varians had 12 fingers so that's why it's in base 12.
class EruTime(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when presed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time display.
        self.message = Label(self.frameBottom, text = "test", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive loop that keeps time updating 
        #   until program is quit or closed.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Displays the calculated Eru'varian time and updates it.
    def timeUpdate(self):
        #88400 seconds in an Eru'varian day.
        #Fetches unix time and converts it to Eru'varian time and displays it.
        self.message["text"] = self.eruConv(time.time())
        self.message.after(1, self.timeUpdate)

    #Takes in the unix time stamp and calculates the Eru'varian time from it.
    def eruConv(self, unix):
        #Net seconds calculated.
        eruSecTotal = unix % 88400

        #Fraction numbers of day calculated.
        twelfth = 88400 / 12
        onefortyfourth = 88400 / 144
        oneseventeentwentyeigth = 88400 / 1728
        onetwentyK = 88400 / 20736
        onetwofiftyK = 88400 / 248832

        #Calculates each base 12 decimal place of the Eru'varian clock.
        twelfths = eruSecTotal // twelfth
        reducedEruSecI = eruSecTotal % twelfth
        onefortyfourths = reducedEruSecI // onefortyfourth
        reducedEruSecII = reducedEruSecI % onefortyfourth
        oneseventeentwentyeigths = reducedEruSecII // oneseventeentwentyeigth
        reducedEruSecIII = reducedEruSecII % oneseventeentwentyeigth
        onetwentyKs = reducedEruSecIII // onetwentyK
        reducedEruSecIV = reducedEruSecIII % onetwentyK
        onetwofiftyKs = reducedEruSecIV // onetwofiftyK

        #Converts each place to base 12 to be displayed.
        base = baseConvertClass.BaseConvert()
        firstPlace = base.baseConv(int(twelfths), 12)
        secondPlace = base.baseConv(int(onefortyfourths), 12)
        thirdPlace = base.baseConv(int(oneseventeentwentyeigths), 12)
        fourthPlace = base.baseConv(int(onetwentyKs), 12)
        fifthPlace = base.baseConv(int(onetwofiftyKs), 12)

        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        return timeString

def main():
    root = Tk()
    root.title("Eru'varian Clock")
    metric = EruTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
