#Jesse A. Jones
#Version: 2022-10-19

#This class contains a method 
#   to find if a year is a leap year or not.
#This is meant to be used as a library to be importet to other programs.
class IsLeap():

    #Determines if given year is a leap year.
    def isLeapYear(self, year):
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        else:
            leap = False
        return leap