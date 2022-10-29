from tkinter import *
import dateHandling
import metricTime

class metricCountDown(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Times 55")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Ariel 55", anchor = "w")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Times 55")
        self.month.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Ariel 55", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Times 55")
        self.day.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 55")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 55")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Ariel 55", command = self.calcMetric)
        self.convButton.grid(row = 6, column = 0)

        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Times 55")
        self.mOutput.grid(row = 6, column = 1)

        self.isStupid = True

    def quitButtonAction(self):
        self.window.destroy()

    def calcMetric(self):
        date = dateHandling.GetDate()
        metric = metricTime.MetricTime()
        year = date.getYear(self.year.get())
        month = date.getMonth(self.month.get())
        day = date.getDay(self.day.get())
        hour = date.getHour(self.hour.get())
        minute = date.getMinOrSec(self.minute.get())
        metricDateFinal = metric.metric_calc(year, month, day, hour, minute)
        metricDateInitial = metric.metric_time()
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
