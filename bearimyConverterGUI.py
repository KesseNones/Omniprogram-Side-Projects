#Jesse A. Jones
#Version: 2022-12-11.1

from tkinter import *
from random import choice
import dateHandling

#Holds methods and members for a program that converts 
#   an amount of Earth time elapsed, into Jearimy Bearimies.
#   Jearimy Bearimies are a reference to how time works 
#   in the Afterlife in the show "The Good Place"
#Like the other projects in this repo, this was made for fun.
class bearimyCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds entires and calculation button, as well as output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Years elapsed field.
        self.messageI = Label(self.frameBottom, text = "Years Elapsed:", font = "Times 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.yearI = Entry(self.frameBottom, font = "Times 20")
        self.yearI.grid(row = 0, column = 1)

        #Days Elapsed Field.
        self.messageIII = Label(self.frameBottom, text = "Days Elapsed:", font = "Times 20", anchor = "w")
        self.messageIII.grid(row = 2, column = 0)
        self.dayI = Entry(self.frameBottom, font = "Times 20")
        self.dayI.grid(row = 2, column = 1)

        #Hours elapsed field.
        self.messageIV = Label(self.frameBottom, text = "Hours Elapsed:", font = "Times 20", anchor = "w")
        self.messageIV.grid(row = 3, column = 0)
        self.hourI = Entry(self.frameBottom, font = "Times 20")
        self.hourI.grid(row = 3, column = 1)

        #Minutes elapsed field.
        self.messageV = Label(self.frameBottom, text = "Minutes Elapsed:", font = "Times 20", anchor = "w")
        self.messageV.grid(row = 4, column = 0)
        self.minuteI = Entry(self.frameBottom, font = "Times 20")
        self.minuteI.grid(row = 4, column = 1)
    
        #Seconds elapsed field.
        self.messageVI = Label(self.frameBottom, text = "Seconds Elapsed:", font = "Times 20", anchor = "w")
        self.messageVI.grid(row = 5, column = 0)
        self.secondI = Entry(self.frameBottom, font = "Times 20")
        self.secondI.grid(row = 5, column = 1)

        #Conversion button.
        self.convButton = Button(self.frameBottom, text = "Convert to Bearimies", 
            font = "Times 20", command = self.eTimeToBer)
        self.convButton.grid(row = 6, column = 0)

        #Output of Jearimy Bearimies elapsed.
        self.bOutput = Label(self.frameBottom, text = "", 
            font = "Times 20", wraplength = 600)
        self.bOutput.grid(row = 6, column = 1)

        #Bearimies elapsed field.
        self.messageVII = Label(self.frameBottom, text = "Bearimies Elapsed:", font = "Times 20", anchor = "w")
        self.messageVII.grid(row = 8, column = 0)
        self.ber = Entry(self.frameBottom, font = "Times 20")
        self.ber.grid(row = 8, column = 1)

        #Button that calls function to convert elapsed Bearimies to elapsed Earth time.
        self.convButton = Button(self.frameBottom, text = "Convert to Relative Earth Time", 
            font = "Times 20", command = self.BerToETime)
        self.convButton.grid(row = 9, column = 0)

        #Displays Earth time elapsed.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Times 20", wraplength = 600)
        self.tOutput.grid(row = 9, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def BerToETime(self):
        eTimeArr = self.berConv(True)
        self.tOutput["text"] = f"{eTimeArr[0]}yr {eTimeArr[1]}d {eTimeArr[2]}hr {eTimeArr[3]}m {eTimeArr[4]}s"
         
    def eTimeToBer(self):
        bearimy = self.berConv(False)
        self.bOutput["text"] = f"{bearimy[0]} Jeremy Bearimies"

    def berConv(self, isConvertingToEarthTime):
        inpHandl = dateHandling.GetDate()
        outPutArr = list()

        #Jearimy Bearimies to Earth time elapsed case.
        if isConvertingToEarthTime:
            #Gets user input JB's and determines multiplier via random.choice.
            ber = inpHandl.getGeneral(self.ber.get())
            mult = choice(range(0,3220))
            
            #Initial decimals found.
            yr = ber * mult
            d = (yr - int(yr)) * 365
            hr = (d - int(d)) * 24
            m = (hr - int(hr)) * 60
            sec = (m - int(m)) * 60
            
            #Turns time units into integers with exception 
            #   of second rounded to three decimal places.
            if (yr < 1000000000):
                year = int(yr)
            else:
                year = yr
            day = int(d)
            hour = int(hr)
            minute = int(m)
            sec = round(sec, 3)

            #Time units appended to return array.
            outPutArr.append(year)
            outPutArr.append(day)
            outPutArr.append(hour)
            outPutArr.append(minute)
            outPutArr.append(sec)
        else:
            #Values derived from user input.
            yr = inpHandl.getYear(self.yearI.get())
            d = inpHandl.getYear(self.dayI.get())
            if (d < 0): 
                d = 0
            if (d > 366): 
                d = 366
            hr = inpHandl.getHour(self.hourI.get())
            m = inpHandl.getMinOrSec(self.minuteI.get())
            sec = inpHandl.getMinOrSec(self.secondI.get())

            #Converts input time units to a decimal of years elapsed.
            yrDec = yr + ((d + ((hr + (m / 60) + (sec / 3600)) / 24)) / 365)
            
            #Converts year decimal to JB via random divisor in specified range. 
            ber = yrDec / choice(range(1, 3220))
            ber = round(ber, 12)

            outPutArr.append(ber)

        return outPutArr

def main():
    root = Tk()
    root.title("Jeremy Bearimy Converter")
    star = bearimyCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
