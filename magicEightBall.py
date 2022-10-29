import random
from time import sleep
from tkinter import *
import winsound

class EightBall(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.flipper = Button(self.frameTop, text = "Ask", 
            font = "Ariel 20", command = self.ballUpdate)
        self.flipper.grid(row = 0, column = 1)

        self.onSoundButton = Button(self.frameTop, text = "Sound On", font = "Ariel 20", command = self.soundOn)
        self.onSoundButton.grid(row = 0, column = 2)

        self.offSoundButton = Button(self.frameTop, text = "Sound Off", font = "Ariel 20", command = self.soundOff)
        self.offSoundButton.grid(row = 0, column = 3)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.draw = Canvas(self.window, width = 800, height = 800, bg = "black")
        
        self.triPoints = [20, 120, 780, 120, 400, 780]

        self.draw.create_polygon(self.triPoints, fill = "blue", outline = "blue", width = 2)

        self.canText = self.draw.create_text(400,300, 
            fill = "white", font = "Times 66", text = "", width = 430, justify = "center")
        self.draw.pack()

        self.message = Label(self.frameBottom, text = "", font = "Ariel 75", anchor = "w", wraplength = 400)
        self.message.pack(side = TOP)

    def quitButtonAction(self):
        self.window.destroy()

    def clickSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def ballSounds(self, num):
        if self.soundsAllowed:
            if num == 1:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/1.wav", winsound.SND_ASYNC)
            if num == 2:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/2.wav", winsound.SND_ASYNC)
            if num == 3:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/3.wav", winsound.SND_ASYNC)
            if num == 4:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/4.wav", winsound.SND_ASYNC)
            if num == 5:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/5.wav", winsound.SND_ASYNC)
            if num == 6:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/6.wav", winsound.SND_ASYNC)
            if num == 7:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/7.wav", winsound.SND_ASYNC)
            if num == 8:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/8.wav", winsound.SND_ASYNC)
            if num == 9:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/9.wav", winsound.SND_ASYNC)
            if num == 10:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/10.wav", winsound.SND_ASYNC)
            if num == 11:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/11.wav", winsound.SND_ASYNC)
            if num == 12:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/12.wav", winsound.SND_ASYNC)
            if num == 13:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/13.wav", winsound.SND_ASYNC)
            if num == 14:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/14.wav", winsound.SND_ASYNC)
            if num == 15:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/15.wav", winsound.SND_ASYNC)
            if num == 16:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/16.wav", winsound.SND_ASYNC)
            if num == 17:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/17.wav", winsound.SND_ASYNC)
            if num == 18:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/18.wav", winsound.SND_ASYNC)
            if num == 19:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/19.wav", winsound.SND_ASYNC)
            if num == 20:
                winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/magicEightBallSounds/20.wav", winsound.SND_ASYNC)


    def soundOn(self):
        self.soundsAllowed = True
        self.clickSound()
    
    def soundOff(self):
        self.soundsAllowed = False

    def ballUpdate(self):
        answer = self.eightBallAsk()
        self.draw.itemconfig(self.canText, text = answer)

    def eightBallAsk(self):
        responseType = random.randint(1, 3)
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
                ballOutput = "Cannot predict now."
                self.ballSounds(14)
            if nonComittalChoice == 5:
                ballOutput = "Concentrate and ask again."
                self.ballSounds(15)
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

    def coin_flip(self):
        X = random.randint(0,1)
        if X == 0:
            Y = "Heads"
        elif X == 1:
            Y = "Tails"
        return Y

def main():
    root = Tk()
    root.title("Magic Eight Ball")
    coin = EightBall(root)
    root.mainloop()

if __name__ == "__main__":
    main()
