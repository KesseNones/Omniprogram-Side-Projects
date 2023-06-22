#Jesse A. Jones
#Version: 2023-06-22.89

from tkinter import *
import datetime
import time
import leapDetect
import metricTime
import dateHandling

#This class displays the current date 
#	in the reformed calendar in the form of a calendar page.
class RefCalCalcII(object):
	def __init__(self, window = None):
		self.window = window

		#Holds quit button, conversion button, and date input fields.
		self.frameTop = Frame(self.window)
		self.frameTop.grid(row = 0, column = 0)

		#Quits program when pressed.
		self.quitButton = Button(self.frameTop, text = "Quit",
			font = "Ariel 20", command = self.quitButtonAction)
		self.quitButton.grid(row = 0, column = 0)

		#Variables used in creation of frames.
		FRAME = self.frameTop
		FONT = "Ariel 20"

		#Year input field.
		self.messageI = Label(FRAME, text = "Enter Year: ", font = FONT)
		self.messageI.grid(row = 1, column = 0)
		self.year = Entry(FRAME, font = FONT)
		self.year.grid(row = 2, column = 0)

		#Month input field.
		self.messageI = Label(FRAME, text = "Enter Month: ", font = FONT)
		self.messageI.grid(row = 3, column = 0)
		self.month = Entry(FRAME, font = FONT)
		self.month.grid(row = 4, column = 0)

		#Day input field.
		self.messageI = Label(FRAME, text = "Enter Day: ", font = FONT)
		self.messageI.grid(row = 5, column = 0)
		self.day = Entry(FRAME, font = FONT)
		self.day.grid(row = 6, column = 0)
		
		#Calculates date of reformed calendar when pressed.
		self.convButton = Button(FRAME, text = "Convert to Reformed Calendar", 
			font = FONT, command = self.userInputCalc)
		self.convButton.grid(row = 7, column = 0)

		#Used for holding the month and year tile.
		self.frameMiddle = Frame(self.window)
		self.frameMiddle.grid(row = 1, column = 0)

		#Holds calendar page display.
		self.frameBottom = Frame(self.window)
		self.frameBottom.grid(row = 2, column = 0)

		#Used in leap year detection, day 
		#	of year calculation, and input date parsing.
		self.leap = leapDetect.IsLeap()
		self.metricAssist = metricTime.MetricTime()
		self.dateParse = dateHandling.GetDate()

		#Lists and boolean used in creation of reformed calendar page.
		self.titleAndWeekArr = []
		self.tileArray = []

		#Calculates current reformed calendar date and displays it.
		
		#Fetches current date and time and stores them in lists.
		self.localTime = datetime.datetime.now()
		dateArr = [self.localTime.year, self.localTime.month, self.localTime.day]
		
		self.createCalendarPage(dateArr)

	#Quits program when called.
	def quitButtonAction(self):
		self.window.destroy()

	def userInputCalc(self):
		year = self.dateParse.getYear(self.year.get())
		month = self.dateParse.getMonth(self.month.get())
		day = self.dateParse.getDay(self.day.get())

		self.destroyCalendarPage()
		self.createCalendarPage([year, month, day])

	#Creates calendar page based on input date array.
	def createCalendarPage(self, dateArray):
		#Calculates reformed calendar date based on input date.
		calArr = self.calcRef(dateArray)
		
		#Finds month index and establishes quad list and week day name list.
		monthIndex = calArr[2] - 1 
		rMonthNameArr = ["Unuary", "Duotober", "Tres", "Quadtober", "Quintecember", 
			"Sixril", "Septecember", "Octo", "Novembuary", 
			"Decemptober", "Undecimber", "Dosdecimber", "Tridecimber", "Supplementary"]
		rWeekNameArr = ["Solday", "Hermesday", "Venusday", 
			"Terraday", "Lunaday", "Marsday", "Joviday"]
		epochLs = ["Before Human Epoch", "Human Epoch"]

		#Creates tile with information 
		#	that represents the title of the calendar.
		title = Tile(self.frameMiddle, 
			f"{rMonthNameArr[monthIndex]} {calArr[1]}\nAge: {calArr[0]} {epochLs[calArr[0] > -1]}", 
			0, 0, font = "Times 30", height = 2, width = 35)
		self.titleAndWeekArr.append(title)

		#If the index is the last one, 
		#	a special supplementary calendar page is created. 
		#	Otherwise, the standard 28 day page is made.
		if (monthIndex == 13):
			self.createSuppPage(calArr)
		else:
			#Creates weekday tiles.
			for i in range(7):
				weekNam = Tile(self.frameBottom, f"{rWeekNameArr[i]}", 1, i)
				self.titleAndWeekArr.append(weekNam)

			#Creates the 28 days of the month.
			monthNum = 1
			for x in range(4):
				for y in range(7):
					dayTile = Tile(self.frameBottom, f"{monthNum}", x + 2, y)
					self.tileArray.append(dayTile)
					monthNum += 1

		#Sets the current day to yellow and completed days to darker gray.
		day = calArr[3]
		pos = 1
		while (pos < day):
			(self.tileArray[pos - 1]).msgTile["bg"] = "#bebebe"
			pos += 1
		(self.tileArray[day - 1]).msgTile["bg"] = "yellow"

	#Creates the supplementary calendar page if needed.
	def createSuppPage(self, calArr):
		#The two week day names possible for supplementary.
		specialWeekNamArr = ["Yearday", "Leapday"]

		#Creates weekdays and the up to two days of the calendar.
		for i in range(1 + self.leap.isLeapYear(calArr[1])):
			weekNamSpecil = Tile(self.frameBottom, f"{specialWeekNamArr[i]}", 1, i)
			self.titleAndWeekArr.append(weekNamSpecil)
			dayTile = Tile(self.frameBottom, f"{i + 1}", 2, i)
			self.tileArray.append(dayTile)
		return

	#Calculates the reformed calendar based on input date.
	def calcRef(self, dateArray):
		#Date input given and day number of year found.
		year = dateArray[0]
		month = dateArray[1]
		day = dateArray[2]
		dayNum = self.metricAssist.findDayNumOfYear(year, month, day) - 1

		#Calculates year with age component.
		rYear = year + 10000
		negMul = [1, -1][rYear < 0]
		subYear = ((rYear) % 10000)
		age = ((rYear) // 10000)

		#Caclulates reformed calendar date elements.
		rMonth = (dayNum // 28) + 1
		rDay = (dayNum % 28) + 1

		return [age, subYear, rMonth, rDay]

	#Destroys the calendar page when called.
	def destroyCalendarPage(self):
		for el in self.titleAndWeekArr:
			el.msgTile.destroy()
		for tile in self.tileArray:
			tile.msgTile.destroy()
		self.titleAndWeekArr = []
		self.tileArray = []

#This class represents a tile of the calendar used 
#	to hold a day number or piece of calendar information.
class Tile():
	def __init__(self, frame, text, row, col, 
		background = "#f0f0f0", font = "Times 17", 
		borderThicc = 0.5, rel = "solid", height = 2, width = 9):

		#Label created and gridded to actually hold 
		#	the information passed to the constructor.
		self.msgTile = Label(frame, text = text, font = font, 
			bg = background, borderwidth = borderThicc, 
			relief = rel, height = height, width = width)
		self.msgTile.grid(row = row, column = col)

def main():
	root = Tk()
	root.title("Reformed Calendar Calculator II")
	metric = RefCalCalcII(root)
	root.mainloop()

if __name__ == "__main__":
	main()