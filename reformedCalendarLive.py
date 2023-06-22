#Jesse A. Jones
#Version: 2023-06-22.93

from tkinter import *
import datetime
import time
import leapDetect
import metricTime

#This class displays the current date 
#	in the reformed calendar in the form of a calendar page.
class RefCalLive(object):
	def __init__(self, window = None):
		self.window = window

		#Holds quit button.
		self.frameTop = Frame(self.window)
		self.frameTop.pack(side = TOP)

		#Quits program when pressed.
		self.quitButton = Button(self.frameTop, text = "Quit",
			font = "Ariel 20", command = self.quitButtonAction)
		self.quitButton.grid(row = 0, column = 0)

		#Holds calendar page display.
		self.frameBottom = Frame(self.window)
		self.frameBottom.pack(side = BOTTOM)

		#Used in leap year detection and day of year calculation.
		self.leap = leapDetect.IsLeap()
		self.metricAssist = metricTime.MetricTime()

		#Lists and boolean used in creation of reformed calendar page.
		self.titleAndWeekArr = []
		self.tileArray = []
		self.isFirstCreated = False

		#Starts recursive time update loop.
		self.timeTrack()

	#Quits program when called.
	def quitButtonAction(self):
		self.window.destroy()

	#Gets the current date, converts to reformed calendar, and displays result.
	def timeTrack(self):
		#Fetches current date and time and stores them in lists.
		self.localTime = datetime.datetime.now()
		dateArr = [self.localTime.year, self.localTime.month, self.localTime.day]
		timeArr = [self.localTime.hour, self.localTime.minute, self.localTime.second]
		
		#Creates calendar page if it hasn't been made yet.
		if not(self.isFirstCreated):
			self.createCalendarPage(dateArr)
			self.isFirstCreated = True

		#If it's 0:00 hours, 
		#	destroy and remake the calendar page 
		#	to update the day.
		if (timeArr[0] == 0 and timeArr[1] == 0):
			self.destroyCalendarPage()
			self.createCalendarPage(dateArr)

		#Recursively loops after a second.
		self.window.after(1000, self.timeTrack)

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
		title = Tile(self.frameTop, 
			f"{rMonthNameArr[monthIndex]} {calArr[1]}\nAge: {calArr[0]} {epochLs[calArr[0] > -1]}", 
			1, 0, font = "Times 30", height = 2, width = 35)
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
		for i in range(1 + self.leap.isLeapYear(calArr[0])):
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
		subYear = ((rYear * negMul) % 10000) * negMul
		age = ((rYear * negMul) // 10000) * negMul

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
	root.title("Live Reformed Calendar")
	metric = RefCalLive(root)
	root.mainloop()

if __name__ == "__main__":
	main()