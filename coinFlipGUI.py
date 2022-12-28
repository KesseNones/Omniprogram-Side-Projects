#Jesse A. Jones
#Version: 2022-12-28.1

from random import randint
from tkinter import *
from time import sleep

#Contains the members and methods necessary 
#   to yield the result of a coin flip, 
#   being Heads or Tails.
class CoinFlip(object):
    def __init__(self, window = None):
        self.window = window

        #Contains the quit button and flip button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        self.flipper = Button(self.frameTop, text = "Flip Coin", 
            font = "Ariel 20", command = self.coinUpdate)
        self.flipper.pack(side = LEFT)

        #Contains the output from a given flip.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Output of flip.
        self.message = Entry(self.frameBottom, font = "Times 30", justify = CENTER)
        self.message.pack(side = TOP)

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Flips the coin and displays the result to the user.
    def coinUpdate(self):
        flip = self.flipCoin()

        #Displays progress message before displaying output to user.
        self.message.delete(0, "end")
        self.message.insert(0, "Flipping...")
        self.message.update()
        sleep(1)
        self.message.delete(0, "end")
        self.message.insert(0, flip)

    #Uses random's randint method to 'randomly' 
    #   choose between a head or tail side.
    def flipCoin(self):
        posArr = ["Heads", "Tails"]
        return posArr[randint(0, 1)]

def main():
    root = Tk()
    root.title("Coin Flipper")
    coin = CoinFlip(root)
    root.mainloop()

if __name__ == "__main__":
    main()
