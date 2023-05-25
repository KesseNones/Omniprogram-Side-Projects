#Jesse A. Jones
#Version: 2023-05-25.91

from tkinter import *
import dateHandling
import metricTime

#This class displays a program that takes in an input date 
#   and displays the number of days until or from the input date.
class metricCountDown(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, countdown starter, and countdown output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Ariel 20", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Ariel 20", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 20", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Ariel 20")
        self.minute.grid(row = 5, column = 1)
    
        #Countdown starting button.
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Ariel 20", command = self.calcMetric)
        self.convButton.grid(row = 6, column = 0)

        #Countdown output field.
        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.mOutput.grid(row = 6, column = 1)
        
        #Used in parsing input date and calculating metric date.
        self.date = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates metric countdown.
    def calcMetric(self):
        #Fetches date and time input.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())
        hour = self.date.getHour(self.hour.get())
        minute = self.date.getMinOrSec(self.minute.get())

        #Calculates final and initial metric dates 
        #   based on current input and current time.
        metricDateFinal = metric.metric_calc(year, month, day, hour, minute)
        metricDateInitial = metric.metric_time()
        
        #Time delta between two metric dates turned into day count 
        #   and result is displayed before recursive loop occurs.
        metricCount = metricDateFinal - metricDateInitial
        metricCount = abs(metricCount) * 1000
        metricCount = format(metricCount, ".6f")
        self.mOutput["text"] = metricCount
        self.mOutput.after(1, self.calcMetric)

def main():
    root = Tk()
    root.title("Metric Date Countdown Timer")
    metric = metricCountDown(root)
    root.mainloop()

if __name__ == "__main__":
    main()
