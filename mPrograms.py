#Jesse A. Jones
#Version: 2023-06-13.17

from tkinter import *
import metricDateGUILIVE
import differentMetricDateCalc
import metricStopwatch
import metricCountDown
import newMoonPhaseCalc
import magicEightBall
import minecraftCalCalc
import mayanLongCount
import nineMaker
import metricDateToDate

#Holds programs that start with the letter M.
class M(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 30", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.metricButtonII = Button(self.frameBottom, text = "Metric Date",
            font = "Ariel 30", command = self.metricDateLiveAct)
        self.metricButtonII.grid(row = 0, column = 0)

        self.metricButton = Button(self.frameBottom, text = "Metric Date Calculator", 
            font = "Ariel 30", command = self.metricCalculator)
        self.metricButton.grid(row = 0, column = 1)

        self.stopwatchButton = Button(self.frameBottom, text = "Metric Stopwatch", 
            font = "Ariel 30", command = self.stopwatch)
        self.stopwatchButton.grid(row = 0, column = 2)

        self.countdownButton = Button(self.frameBottom, text = "Metric Countdown", 
            font = "Ariel 30", command = self.metricCountDown)
        self.countdownButton.grid(row = 1, column = 0)

        self.moonButton = Button(self.frameBottom, text = "Moon Phase Calculator MK II", 
            font = "Ariel 30", command = self.moonCalc)
        self.moonButton.grid(row = 1, column = 1)
    
        self.eightButton = Button(self.frameBottom, text = "Magic Eight Ball", 
            font = "Ariel 30", command = self.magicEightBall)
        self.eightButton.grid(row = 1, column = 2)

        self.craftmineButton = Button(self.frameBottom, text = "Minecraft Calendar Calc", 
            font = "Ariel 30", command = self.mcCalc)
        self.craftmineButton.grid(row = 2, column = 0)

        self.mayaButton = Button(self.frameBottom, text = "Mayan Long Count Calendar Calc", 
            font = "Ariel 30", command = self.mayanCalc)
        self.mayaButton.grid(row = 2, column = 1)

        self.nineButton = Button(self.frameBottom, text = "Maker of Nines", 
            font = "Ariel 30", command = self.makeNines)
        self.nineButton.grid(row = 2, column = 2)
        
        self.metricToNormButton = Button(self.frameBottom, text = "Metric Date to Normal Date",
            font = "Ariel 30", command = self.toNormConv)
        self.metricToNormButton.grid(row = 3, column = 0)

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    def metricDateLiveAct(self):            #DONE
        metricDateGUILIVE.main()

    def metricCalculator(self):             #DONE
        differentMetricDateCalc.main()

    def stopwatch(self):                    #DONE
        metricStopwatch.main()

    def metricCountDown(self):              #DONE
        metricCountDown.main()

    def moonCalc(self):                     #DONE
        newMoonPhaseCalc.main()

    def magicEightBall(self):               #DONE
        magicEightBall.main()

    def mcCalc(self):                       #DONE
        minecraftCalCalc.main()

    def mayanCalc(self):                    #DONE
        mayanLongCount.main()

    def makeNines(self):                    #DONE
        nineMaker.main()

    def toNormConv(self):                   #DONE
        metricDateToDate.main()

def main():
    root = Tk()
    root.title("Programs That Start With M")
    om = M(root)
    root.mainloop()

if __name__ == "__main__":
    main()