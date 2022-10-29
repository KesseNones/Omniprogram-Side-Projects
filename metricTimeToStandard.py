import leapDetect
class MetricToStandard():
    def __init__(self):
        self.leap = leapDetect.IsLeap()

    def metricToStandard(self, metric, isFloat = False):
        yearCycleCount = metric // 146097
        metric %= 146097
        yearCount = int(self.determineYears(metric) + (400 * yearCycleCount))
        #metric = metric % 146097
        metric -= self.daysToSubtract
        weekCount = int(metric // 7)
        metric %= 7
        dayCount = int(metric)
        metric -= dayCount
        daySec = metric * 86400
        hourCount = int(daySec // 3600)
        daySec %= 3600
        minCount = int(daySec // 60)
        daySec %= 60
        secCount = int(daySec)

        if isFloat:
            yearCount = float(yearCount)

        string = str(yearCount) + "yr " + str(weekCount).zfill(2) + "wk " + str(dayCount) + "d " + str(hourCount).zfill(2) + "h " + str(minCount).zfill(2) + "m " + str(secCount).zfill(2)
        return string

    def determineYears(self, metric):
        intMetric = int(metric)
        self.daysToSubtract = 0
        year = 0
        while intMetric > 365:
            leap = self.leap.isLeapYear(year)
            if leap:
                sub = 366
            else:
                sub = 365
            year += 1
            intMetric -= sub
            self.daysToSubtract += sub
        return year