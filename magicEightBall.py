#Jesse A. Jones
#Version: 2023-05-26.16

import random
from tkinter import *
from playsound3 import playsound

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
            playsound("magicEightBallSounds/click.wav", False)

    #Plays an appropriate magic eight ball sound based on the input number.
    def ballSounds(self, num):
        if self.soundsAllowed:
            if 0 < num < 21:
                playsound(f"magicEightBallSounds/{num}.wav", False)

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
        #Lists used to contain all responses.
        positiveResponses = ["It is certain.", "It is decidedly so.", "Without a doubt.", \
                            "Yes - definitely.", "You may rely on it.", "As I see it, yes.", \
                            "Most likely.", "Outlook good.", "Yes", "Signs point to yes."]
        neutralResponses = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", \
                            "Cannot predict\n now.", "Concentrate\n and ask again."]
        negativeResponses = ["Don't count on it.", "My reply is no.", "My sources say no.", \
                            "Outlook not so good.", "Very doubtful."]

        #Randomly picks response type.
        responseType = random.randint(1, 3)

        #Positive answers.
        if responseType == 1:
            affirmativeChoice = random.randint(1, 10)
            ballOutput = positiveResponses[affirmativeChoice - 1]
            self.ballSounds(affirmativeChoice)

        #Neutral answers.
        elif responseType == 2:
            nonComittalChoice = random.randint(1,5)
            ballOutput = neutralResponses[nonComittalChoice - 1]
            self.ballSounds(nonComittalChoice + 10)

        #Negative answers.
        else:
            negativeChoice = random.randint(1,5)
            ballOutput = negativeResponses[negativeChoice - 1]
            self.ballSounds(negativeChoice + 15)

        return ballOutput

def main():
    root = Tk()
    root.title("Magic Eight Ball")
    coin = EightBall(root)
    root.mainloop()

if __name__ == "__main__":
    main()
