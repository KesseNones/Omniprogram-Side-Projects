#Jesse A. Jones
#Version: 2023-05-26.10

import random
from tkinter import *
import winsound

#This class displays a magic eight ball 
#   that randomly displays answers to a user's verbal or mental questions.
class EightBall(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        #Holds quit button, ask button, and sound toggle buttons.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when clicked.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Activates magic eight ball when clicked.
        self.flipper = Button(self.frameTop, text = "Ask", 
            font = "Ariel 20", command = self.ballUpdate)
        self.flipper.grid(row = 0, column = 1)

        #Enables sound when clicked.
        self.onSoundButton = Button(self.frameTop, text = "Sound On", font = "Ariel 20", command = self.soundOn)
        self.onSoundButton.grid(row = 0, column = 2)

        #Disables sound when clicked. Sound is disabled by default.
        self.offSoundButton = Button(self.frameTop, text = "Sound Off", font = "Ariel 20", command = self.soundOff)
        self.offSoundButton.grid(row = 0, column = 3)

        #Holds display of magic eight ball.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Colored background that looks like magic eight ball.
        self.draw = Canvas(self.window, width = 400, height = 400, bg = "black")
        self.draw.create_polygon([10, 60, 390, 60, 200, 390], fill = "blue", outline = "blue", width = 2)

        #Displays magic eight ball text.
        self.canText = self.draw.create_text(200, 150, 
            fill = "white", font = "Ariel 33", text = "", width = 240, justify = "center")
        self.draw.pack()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Plays click sound for certain things.
    def clickSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("magicEightBallSounds/click.wav", winsound.SND_ASYNC)

    #Plays an appropriate magic eight ball sound based on the input number.
    def ballSounds(self, num):
        if self.soundsAllowed:
            if 0 < num < 21:
                winsound.PlaySound(f"magicEightBallSounds/{num}.wav", winsound.SND_ASYNC)

    #Turns sound on when called.
    def soundOn(self):
        self.soundsAllowed = True
        self.clickSound()
    
    #Turns sound off when called.
    def soundOff(self):
        self.soundsAllowed = False

    #Generates magic eight ball answer and updates text.
    def ballUpdate(self):
        answer = self.eightBallAsk()
        self.draw.itemconfig(self.canText, text = answer)

    #Generates magic eight ball answer.
    def eightBallAsk(self):

        #Randomly picks response type.
        responseType = random.randint(1, 3)

        #Positive answers.
        if responseType == 1:
            affirmativeChoice = random.randint(1, 10)
            if affirmativeChoice == 1:
                ballOutput = "It is certain."
                self.ballSounds(1)
            if affirmativeChoice == 2:
                ballOutput = "It is decidedly so."
                self.ballSounds(2)
            if affirmativeChoice == 3:
                ballOutput = "Without a doubt."
                self.ballSounds(3)
            if affirmativeChoice == 4:
                ballOutput = "Yes - definitely."
                self.ballSounds(4)
            if affirmativeChoice == 5:
                ballOutput = "You may rely on it."
                self.ballSounds(5)
            if affirmativeChoice == 6:
                ballOutput = "As I see it, yes."
                self.ballSounds(6)
            if affirmativeChoice == 7:
                ballOutput = "Most likely."
                self.ballSounds(7)
            if affirmativeChoice == 8:
                ballOutput = "Outlook good."
                self.ballSounds(8)
            if affirmativeChoice == 9:
                ballOutput = "Yes."
                self.ballSounds(9)
            if affirmativeChoice == 10:
                ballOutput = "Signs point to yes."
                self.ballSounds(10)

        #Neutral answers.
        elif responseType == 2:
            nonComittalChoice = random.randint(1,5)
            if nonComittalChoice == 1:
                ballOutput = "Reply hazy, try again."
                self.ballSounds(11)
            if nonComittalChoice == 2:
                ballOutput = "Ask again later."
                self.ballSounds(12)
            if nonComittalChoice == 3:
                ballOutput = "Better not tell you now."
                self.ballSounds(13)
            if nonComittalChoice == 4:
                ballOutput = "Cannot predict\n now."
                self.ballSounds(14)
            if nonComittalChoice == 5:
                ballOutput = "Concentrate\n and ask again."
                self.ballSounds(15)

        #Negative answers.
        else:
            negativeChoice = random.randint(1,5)
            if negativeChoice == 1:
                ballOutput = "Don't count on it."
                self.ballSounds(16)
            if negativeChoice == 2:
                ballOutput = "My reply is no."
                self.ballSounds(17)
            if negativeChoice == 3:
                ballOutput = "My sources say no."
                self.ballSounds(18)
            if negativeChoice == 4:
                ballOutput = "Outlook not so good."
                self.ballSounds(19)
            if negativeChoice == 5:
                ballOutput = "Very doubtful."
                self.ballSounds(20)
                
        return ballOutput

def main():
    root = Tk()
    root.title("Magic Eight Ball")
    coin = EightBall(root)
    root.mainloop()

if __name__ == "__main__":
    main()
