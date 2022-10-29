#Jesse A. Jones
#Version: 2022-10-19

#This class is used to handle date input.
#GetDate is intended to be used as an imported class in other programs.
class GetDate():

    #Used in parsing an input intendet to be a year.
    def getYear(self, year, isFloat = False):

        #Handles empty string cases.
        if (isFloat == False):
            if year == "":
                return 0
            else:
                return int(year)
        else:
            if year == "":
                return float(0)
            else:
                return float(year)
    
    #Used in parsing month input.
    def getMonth(self, month):
        #Empty string case.
        if month == "":
            return 1
        month = int(month)

        #Month out of range case.
        if month > 12 or month < 1:
            return 1
        else:
            return month

    #Used in parsing day input.
    def getDay(self, day):
        #Day empty string case.
        if day == "":
            return 1
        day = int(day)

        #Day out of range case.
        if day > 31 or day < 1:
            return 1
        else:
            return day

    #Used in parsing hour input.
    def getHour(self, hour):
        #Empty hour string case.
        if hour == "":
            return 0
        hour = int(hour)

        #Out of range hour case.
        if hour > 23 or hour < 0:
            return 0
        else:
            return hour

    #Used in parsing minute or second input.
    def getMinOrSec(self, time):
        #Empty minute/second case.
        if time == "":
            return 0
        time = int(time)

        #Out of range minute/second case.
        if time > 60 or time < 0:
            return 0
        else:
            return time

    #Used in processing general input.
    def getGeneral(self, inp):
        if inp == "":
            return 0
        else:
            return float(inp)