#Jesse A. Jones
#Version: 2023-05-31.07

from tkinter import *
import dateHandling
import metricTime

#This class takes in an input date 
#   and displays the resulting mayan long count, tzolkin, and haab.
class MayanCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Used in metric date calculations.
        self.isStupid = True

        #Holds date input fields, conversion button, and converted output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.yearE = Entry(self.frameBottom, font = "Ariel 20")
        self.yearE.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.monthE = Entry(self.frameBottom, font = "Ariel 20")
        self.monthE.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.dayE = Entry(self.frameBottom, font = "Ariel 20")
        self.dayE.grid(row = 3, column = 1)
    
        #Converts input date to mayan calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Mayan Calendar", 
            font = "Ariel 20", command = self.MCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #Outputs the Mayan long count date.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutput.grid(row = 4, column = 1)

        #Outputs the Mayan Tzolkin, Haab, and Lord of the Night.
        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputII.grid(row = 5, column = 1)

        #Used for date parsing and metric time calculations.
        self.dateGet = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function to convert input date 
    #   to Mayan calendar and displays result.
    def MCalCalc(self):
        dateArr = self.mayCalc()
        self.cOutput["text"] = dateArr[0]
        self.cOutputII["text"] = dateArr[1]

    #Pefroms the calculations and function 
    #   calls necessary to calculate mayan calendar.
    def mayCalc(self):
        #Fetches date input.
        year = self.dateGet.getYear(self.yearE.get())
        month = self.dateGet.getMonth(self.monthE.get())
        day = self.dateGet.getDay(self.dayE.get())
        
        #Calculates current day of mayan calendar in terms of raw day count.
        dayBase = 2515647
        currentDay = self.metric.metric_calc(year, month, day, 0, 0)
        currentDay = int(currentDay * 1000)
        dayDelta = currentDay - dayBase

        #The day delta is used to calculate 
        #   the mayan long count and tzolkin and haab. 
        #   A list is returned of the long count string 
        #   and Tzolkin and haab string.
        return [self.toMayan(dayDelta), self.toTzolkinAndHaab(dayDelta)]

    #Takes in day delta and calculates Tzolkin and Haab.
    def toTzolkinAndHaab(self, dayDelta):
        #8 Cumku haab base
        
        #God names used in Tzolkin.
        tzolGods = ["Imix", "Ik", "Akbal", "Kan", "Chicchan", "Cimi", "Manik", "Lamat", "Muluc", "Oc", "Chuen", "Eb", "Ben", "Ix", "Men", "Cib", "Caban", "Etznab", "Cauac", "Ahau"]
        
        #Month names of Haab.
        haabMonths = ["Pop", "Uo", "Zip", "Zotz", "Tzec", "Xul", "Yaxkin", "Mol", "Chen", "Yax", "Zac", "Ceh", "Mac", "Kankin", "Muan", "Pax", "Kayab", "Cumku", "Uayeb"]
        
        #Range of days in tzolkin.
        tzolDays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        #The range of numbers who are lords of the night.
        lordOfNightArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        #Base index for each Tzolkin.
        tzolDayIndex = 3
        tzolGodIndex = 19
        
        #Calculates current Tzolkin day.
        currentTzolDay = dayDelta % 260
        #Tzolkin base case.
        if currentTzolDay == 0:
            tzolDay = 4
            tzolGod = "Ahau"

        #Advances time until current Tzolkin is found.
        while currentTzolDay > 0:
            tzolDayIndex += 1
            tzolGodIndex += 1
            #Resets indexes.
            if tzolDayIndex > 12:
                tzolDayIndex %= 13
            if tzolGodIndex > 19:
                tzolGodIndex %= 20
            tzolDay = tzolDays[tzolDayIndex]
            tzolGod = tzolGods[tzolGodIndex]
            currentTzolDay -= 1

        #Calculates date in Haab.
        currentHaabDay = (dayDelta + 348) % 365
        haabMonthNum = currentHaabDay // 20
        haabDay = currentHaabDay % 20
        haabMonth = haabMonths[haabMonthNum]
        
        #Calculates lord of night and returns resulting time string.
        lordOfNightIndex = dayDelta % 9 - 1
        lordOfNightGod = lordOfNightArr[lordOfNightIndex]
        return f"{tzolDay} {tzolGod}, {haabDay} {haabMonth}, G{lordOfNightGod}"

    #Calculates the long count date based on the day delta.
    def toMayan(self, dayDelta):
        #Lengths of each mayan long count section in days.
        alauTunLength = 23040000000
        kinchilTunLength = 1152000000
        kalapTunLength = 57600000
        piktunLength = 2880000
        baktunLength = 144000
        katunLength = 7200
        tunLength = 360
        winalLength = 20
        kinLength = 1
        
        #Alautun calculated.
        alauTun = dayDelta // alauTunLength
        reducedDayDelta = dayDelta % alauTunLength
        
        #KinchilTun calculated.
        kinchilTun = reducedDayDelta // kinchilTunLength
        reducedDayDelta = reducedDayDelta % kinchilTunLength
        
        #Kalaptun calculated.
        kalapTun = reducedDayDelta // kalapTunLength
        reducedDayDelta = reducedDayDelta % kalapTunLength

        #Piktun calculated.
        piktun = reducedDayDelta // piktunLength
        reducedDayDelta = reducedDayDelta % piktunLength

        #Baktun calculated.
        baktun = (reducedDayDelta // baktunLength)
        reducedDayDelta = reducedDayDelta % baktunLength

        #Katun calculated.
        katun = reducedDayDelta // katunLength
        reducedDayDelta %= katunLength

        #Tun calculated.
        tun = reducedDayDelta // tunLength
        reducedDayDelta %= tunLength

        #Winal calculated.
        winal = reducedDayDelta // winalLength
        reducedDayDelta %= winalLength
        
        #Kin is days leftover.
        kin = reducedDayDelta

        #Builds longcount time string and returns it.
        return f"{alauTun}.{kinchilTun}.{kalapTun}.{piktun}.{baktun}.{katun}.{tun}.{winal}.{kin}"

def main():
    root = Tk()
    root.title("Mayan Long Count Calendar Calculator")
    calCalc = MayanCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
