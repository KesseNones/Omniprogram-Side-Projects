from tkinter import *
import datetime
import time
import leapDetect
import metricTime

class RefCalLive(object):
	def __init__(self, window = None):
		self.window = window

		self.frameTop = Frame(self.window)
		self.frameTop.pack(side = TOP)

		self.quitButton = Button(self.frameTop, text = "Quit",
			font = "Ariel 20", command = self.quitButtonAction)
		self.quitButton.grid(row = 0, column = 0)

		self.frameBottom = Frame(self.window)
		self.frameBottom.pack(side = BOTTOM)

		self.leap = leapDetect.IsLeap()
		self.metricAssist = metricTime.MetricTime()
		self.titleAndWeekArr = []
		self.tileArray = []
		self.isFirstCreated = False

		self.timeTrack()

	def quitButtonAction(self):
		self.window.destroy()

	def timeTrack(self):
		self.localTime = datetime.datetime.now()
		dateArr = [self.localTime.year, self.localTime.month, self.localTime.day]
		timeArr = [self.localTime.hour, self.localTime.minute, self.localTime.second]
		if not(self.isFirstCreated):
			self.createCalendarPage(dateArr)
			self.isFirstCreated = True

		if (timeArr[0] == 0 and timeArr[1] == 0):
			self.destroyCalendarPage()
			self.createCalendarPage(dateArr)

		self.window.after(1000, self.timeTrack)

	def createCalendarPage(self, dateArray):
		calArr = self.calcRef(dateArray)
		monthIndex = calArr[1] - 1 
		rMonthNameArr = ["Unuary", "Duotober", "Tres", "Quadtober", "Quintecember", 
			"Sixril", "Septecember", "Octo", "Novembuary", 
			"Decemptober", "Undecimber", "Dosdecimber", "Tridecimber", "Supplementary"]
		rWeekNameArr = ["Solday", "Hermesday", "Venusday", 
			"Terraday", "Lunaday", "Marsday", "Joviday"]

		title = Tile(self.frameTop, 
			f"{rMonthNameArr[monthIndex]} {calArr[0]} H.E.", 
			1, 0, font = "Times 60", height = 2, width = 20)
		self.titleAndWeekArr.append(title)

		if (monthIndex == 13):
			self.createSuppPage(calArr)
		else:
			for i in range(7):
				weekNam = Tile(self.frameBottom, f"{rWeekNameArr[i]}", 1, i)
				self.titleAndWeekArr.append(weekNam)

			monthNum = 1
			for x in range(4):
				for y in range(7):
					dayTile = Tile(self.frameBottom, f"{monthNum}", x + 2, y)
					self.tileArray.append(dayTile)
					monthNum += 1

		day = calArr[2]
		pos = 1
		while (pos < day):
			(self.tileArray[pos - 1]).msgTile["bg"] = "#bebebe"
			pos += 1
		(self.tileArray[day - 1]).msgTile["bg"] = "yellow"

	def createSuppPage(self, calArr):
		specialWeekNamArr = ["Yearday", "Leapday"]
		for i in range(1 + self.leap.isLeapYear(calArr[0])):
			weekNamSpecil = Tile(self.frameBottom, f"{specialWeekNamArr[i]}", 1, i)
			self.titleAndWeekArr.append(weekNamSpecil)
			dayTile = Tile(self.frameBottom, f"{i + 1}", 2, i)
			self.tileArray.append(dayTile)
		return

	def calcRef(self, dateArray):
		year = dateArray[0]
		month = dateArray[1]
		day = dateArray[2]
		dayNum = self.metricAssist.findDayNumOfYear(year, month, day) - 1

		rYear = year + 10000
		rMonth = (dayNum // 28) + 1
		rDay = (dayNum % 28) + 1

		return [rYear, rMonth, rDay]

	def destroyCalendarPage(self):
		for el in self.titleAndWeekArr:
			el.msgTile.destroy()
		for tile in self.tileArray:
			tile.msgTile.destroy()
		self.titleAndWeekArr = []
		self.tileArray = []

class Tile():
	def __init__(self, frame, text, row, col, 
		background = "#f0f0f0", font = "Times 35", 
		borderThicc = 1, rel = "solid", height = 2, width = 9):
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