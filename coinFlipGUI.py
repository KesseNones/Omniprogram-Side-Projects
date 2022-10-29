import random
from time import sleep
from tkinter import *

class CoinFlip(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        self.flipper = Button(self.frameTop, text = "Flip Coin", 
            font = "Ariel 20", command = self.coinUpdate)
        self.flipper.pack(side = LEFT)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Click to Flip", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)

    def quitButtonAction(self):
        self.window.destroy()

    def coinUpdate(self):
        flip = self.coin_flip()
        self.message["text"] = flip

    def coin_flip(self):
        X = random.randint(0,1)
        if X == 0:
            Y = "Heads"
        elif X == 1:
            Y = "Tails"
        return Y

def main():
    root = Tk()
    root.title("Coin Flipper")
    coin = CoinFlip(root)
    root.mainloop()

if __name__ == "__main__":
    main()
