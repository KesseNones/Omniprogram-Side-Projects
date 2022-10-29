#Jesse A. Jones
#Version: 2022-10-19

import time
import datetime
import math
import leapDetect

#This class is used to calculate the metric date 
#   as well as potentially just find the day number from a date.
#This class is meant to be used as a library 
#   with built in functions for use in other programs.
class MetricTime():

    def __init__(self):
        self.leap = leapDetect.IsLeap()

    #Finds metric date from year, day number, hour, and minute.
    def metricCalcII(self, year, dayNum, hour, minute):
        year += 10000
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097

        #Iterates through remaining years and adds 
        #   up all the 365 and 366 day combinations for the years.
        while remainingYears > 0:
            leap = self.leap.isLeapYear(remainingYears)
            if leap:
                totalDays += 366
            else:
                totalDays += 365
            remainingYears -= 1

        #Calculates metric date stamp from net day count.
        totalDays += dayNum - 1
        totalDays = totalDays / 1000
        totalDays = round(totalDays, 3)
        secTotal = (hour * 3600) + (minute * 60)
        dayDec = secTotal / 86400
        dayDec *= 1000000
        dayDec = math.floor(dayDec)
        dayDec = dayDec / 1000000000
        finalMetric = totalDays + dayDec
        return finalMetric 

    #Calculates metric date if it's in a given range of dates.
    def metric_calc(self, year, month, day, hour, minute, isStupid = True):

        #Sets upper and lower bounds for years.
        if isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000

        #If input year is within the range, 
        #   calculate the metric date using the first method,
        #   otherwise calculate using the second.
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
            metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
            rounderI = metric_time * 1000000000
            rounderII = math.trunc(rounderI)
            rounderIII = rounderII / 1000000000
        else:
            dayCount = self.findDayNumOfYear(year, month, day)
            rounderIII = self.metricCalcII(year, dayCount, hour, minute)
        return rounderIII

    #Finds the ordinal day number within a year given a year, month, and day.
    def findDayNumOfYear(self, year, month, day):
        #Determines if year is leap year.
        leap_year = self.leap.isLeapYear(year)
        
        #Finds day number in long conditional chain.
        if month == 1:
                D_Code_MKI = 0
        if month == 2:
                D_Code_MKI = 31
        if month == 3:
                D_Code_MKI = 59
                if leap_year == True:
                    D_Code_MKI = 60
        if month == 4:
                D_Code_MKI = 90
                if leap_year == True:
                    D_Code_MKI = 91
        if month == 5:
                D_Code_MKI = 120
                if leap_year == True:
                    D_Code_MKI = 121
        if month == 6:
                D_Code_MKI = 151
                if leap_year == True:
                    D_Code_MKI = 152
        if month == 7:
                D_Code_MKI = 181
                if leap_year == True:
                    D_Code_MKI = 182
        if month == 8:
                D_Code_MKI = 212
                if leap_year == True:
                    D_Code_MKI = 213
        if month == 9:
                D_Code_MKI = 243
                if leap_year == True:
                    D_Code_MKI = 244
        if month == 10:
                D_Code_MKI = 273
                if leap_year == True:
                    D_Code_MKI = 274
        if month == 11:
                D_Code_MKI = 304
                if leap_year == True:
                    D_Code_MKI = 305
        if month == 12:
                D_Code_MKI = 334
                if leap_year == True:
                    D_Code_MKI = 335

        #Finishes day number calculation.
        D_Code_MKII = D_Code_MKI + day
        
        return D_Code_MKII

    #Calculates the live metric timestamp based on the Unix Timestamp.
    def metric_time(self):
        t = time.time()

        #Converts Unix Epoch Time to Metric Time.
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
        rounderI = metric_time * 1000000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000000
        return rounderIII