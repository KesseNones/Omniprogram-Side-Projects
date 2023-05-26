#Jesse A. Jones
#Version: 2023-05-26.08

from tkinter import *
import metricTime 
import dateHandling

#Takes in an input date and time and calculates the moon phase from it.
class MoonCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, conversion button, and moon phase output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 20", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 20", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Ariel 20")
        self.minute.grid(row = 5, column = 1)
    
        #Moon phase calculation.
        self.convButton = Button(self.frameBottom, text = "Calculate Moon Phase", 
            font = "Ariel 20", command = self.moonCalc)
        self.convButton.grid(row = 6, column = 0)

        #Displays moon age.
        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.mOutput.grid(row = 6, column = 1)

        #Displays moon phase.
        self.mOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.mOutputII.grid(row = 7, column = 1)

        #Objects used in parsing input date and metric time respectively.
        self.parse = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates moon phase based on metric date and displays results.
    def moonCalc(self):
        #Fetches user input.
        year = self.parse.getYear(self.year.get())
        month = self.parse.getMonth(self.month.get())
        day = self.parse.getDay(self.day.get())
        hour = self.parse.getHour(self.hour.get())
        minute = self.parse.getMinOrSec(self.minute.get())

        #Finds current metric date and finds difference from base metric date.
        metricDateCalc = self.metric.metric_calc(year, month, day, hour, minute)
        moonBase = 4390.562679166
        metricDiff = metricDateCalc - moonBase
        
        #Metric delta used to find moon age.
        moonAge = (metricDiff * 1000) % 29.530588
        #Accounts for negative moon age edge case.
        if moonAge < 0:
            moonAge += 29.530588
        
        #Formats moon age decimal.
        moonAgeDisp = round(moonAge, 6)
        moonAgeDisp = format(moonAgeDisp, ".6f")
        
        #Determines which moon phase the moon is currently in.
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "New Moon 🌑"
        elif 3.6913235 <= moonAge < 7.382647:
            moonPhase = "Waxing Crescent 🌒"
        elif 7.382647 <= moonAge < 11.0739705:
            moonPhase = "First Quarter 🌓"
        elif 11.0739705 <= moonAge < 14.765294:
            moonPhase = "Waxing Gibbous 🌔"
        elif 14.765294 <= moonAge < 18.4566175:
            moonPhase = "Full Moon 🌕"
        elif 18.4566175 <= moonAge < 22.147941:
            moonPhase = "Waning Gibbous 🌖"
        elif 22.147941 <= moonAge < 25.8392645:
            moonPhase = "Third Quarter 🌗"
        elif 25.8392645 <= moonAge < 29.530588:
            moonPhase = "Waning Crescent 🌘"
        else:
            moonPhase = "WTF???"

        #Resulting moon age and phase displayed.
        self.mOutput["text"] = moonAgeDisp
        self.mOutputII["text"] = moonPhase

def main():
    root = Tk()
    root.title("Moon Phase Calculator")
    moon = MoonCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
