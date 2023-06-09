#Jesse A. Jones
#Version: 2023-06-09.15

from tkinter import *
import dateHandling
import leapDetect

#This class takes in an input date 
#   and displays the resulting seasonally synched calendar, 
#   a calendar like ours but the dates are 19 days back 
#   and the year starts in march, synching the months better with the seasons.
class SeasonCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when called.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, conversion button, and calendar output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.yearE = Entry(self.frameBottom, font = "Ariel 20")
        self.yearE.grid(row = 1, column = 0)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.monthE = Entry(self.frameBottom, font = "Ariel 20")
        self.monthE.grid(row = 3, column = 0)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 4, column = 0)
        self.dayE = Entry(self.frameBottom, font = "Ariel 20")
        self.dayE.grid(row = 5, column = 0)
    
        #Converts input date to seasonal calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Seasonal Synced Calendar", 
            font = "Ariel 20", command = self.sCalCalc)
        self.convButton.grid(row = 6, column = 0)

        #Displays converted seasonal calendar.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutput.grid(row = 7, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates the seasonal calendar based on input and displays the result.
    def sCalCalc(self):
        dateString = self.cal_calc()
        self.cOutput["text"] = dateString

    #Calculates the reformed calendar and returns the appropriate date string.
    def cal_calc(self):
        #Instances used in parsing input date and determining leap year.
        date = dateHandling.GetDate()
        leap = leapDetect.IsLeap()

        #Input date fetched.
        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())
        
        #Lists used for calendar calculation and display of month.
        monthDayArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthNameArr = ["January", "February", "March", "April", "May", "June", \
                "July", "August", "September", "October", "November", "December"]
        
        #Shifts day back 19 days as per the calendar.
        flag = 0
        day -= 19
        
        #Year decreased and flag is set 
        #   to indicate that it's the previous year.
        if month < 3:
            year -= 1
            flag += 1

        #Accounts for day being less than 1.
        if day < 1:

            month -= 1
            
            #If month is now less than 3 after month is shifted back 
            #   and it isn't already the previous seasonal year, now it is.
            if month < 3 and flag == 0:
                year -= 1
            
            #Compensates for being in the previous gregorian year.
            if month < 1:
                month += 12
            
            #Adds leap day to februrary if it's a leap year.
            if (leap.isLeapYear(year)):
                monthDayArr[1] += 1
            
            #Adds number from list to put day back above 0.
            day += monthDayArr[(month - 1)]
        
        #Constructs date string and returns it.
        dateString = f"{day} {monthNameArr[month - 1]}, {year}"
        return dateString

def main():
    root = Tk()
    root.title("Seasonal Synced Calendar Converter")
    calCalc = SeasonCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
