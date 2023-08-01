#Jesse A. Jones
#Version: 2023-08-01.23

#This class is used to handle date input.
#GetDate is intended to be used as an imported class in other programs.
class GetDate():
    #Used in parsing an input intendet to be a year.
    def getYear(self, year, isFloat = False):
        if isFloat:
            #Tries to cast to float. If it succeeds, casted number is returned. 
            #   In event of failure, 0.0 is returned.
            try:
                return float(year) 
            except ValueError:
                return 0.0
        else:
            #Tries to cast to int. If it succeeds, casted number is returned. 
            #   In event of failure, 0 is returned.
            try:
                return int(year)
            except ValueError:
                return 0
    
    #Used in parsing month input.
    def getMonth(self, month):
        #If casting succeeds, further checking occurs, 
        #   otherwise default value returned.
        try:
            intMonth = int(month)
            return (intMonth if intMonth > 0 and intMonth < 13 else 1)
        except ValueError:
            return 1

    #Parses input day string and returns casted valid day 
    #   or default value of 1.
    def getDay(self, day):
        try:
            intDay = int(day)
            #If casting succeeds, range check occurs and returns 
            #   either casted day or default value if out of range.
            return (intDay if intDay > 0 and intDay < 32 else 1)
        except ValueError:
            return 1

    #Parses input hour string given to it.
    def getHour(self, hour):
        try:
            hourCast = int(hour)
            return (hourCast if hourCast > -1 and hourCast < 24 else 0)
        except ValueError:
            return 0

    #Used in parsing minute or second input.
    def getMinOrSec(self, time):
        try:
            timeCast = int(time)
            return (timeCast if timeCast > -1 and timeCast < 60 else 0)
        except ValueError:
            return 0

    #Used in processing general input.
    def getGeneral(self, inp):
        try:
            return float(inp)
        except ValueError:
            return 0.0