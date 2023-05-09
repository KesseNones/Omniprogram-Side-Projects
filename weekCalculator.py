#Jesse A. Jones
#Version: 2023-05-09.87

import leapDetect

#This class calculates a weekday of a date passed in it.
class WeekFinder():
	def __init__():
		self.leap = leapDetect.IsLeap()

	#Finds day of week from input year, month, and day.
	def weekFind(self, year, month, day):
	    #Determines if 1 needs to be subtracted from calculations or not.

	    #Useful arrays for calculating week stuff.
	    centuryCodeArr = [6, 4, 2, 0]
	    monthCodeArr = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
	    weekNameArr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	    #Numbers used in the week calculation.
	    leapSubtract = 0 - ((month < 3) and self.leap.isLeapYear(year))
	    cenCode = centuryCodeArr[(year // 100) % 4]
	    monthCode = monthCodeArr[month - 1]
	    decAndYr = year % 100
	    yearNum = decAndYr + (decAndYr // 4)

	    return weekNameArr[((cenCode + yearNum + monthCode + day + leapSubtract) % 7)]