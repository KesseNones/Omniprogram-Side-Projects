# Omniprogram Side Projects
Created By Jesse A. Jones
## Introduction
The Omniprogram is a collection of dozens of converters 
and other random tools I felt were useful to make for myself.
This program has been assembled over the course of years of messing around with Python, 
first in terminal format programs and then in GUI form after learning about tkinter.
This repositorty is a compilation of all such programs as well as an executable version to run on windows.
## How to Run
There are multiple ways to run the Omniprogram for use.

### 1. The Executable
The first and most obvious way to run Omniprogram is by downloading the ```omniprogramExecutableVersion```
folder, unzipping it, going to the ```dist``` subfolder, and running the executable contained within.
This will open up the main program menu which can be used to run all the programs.

### 2. The Interpreted Version
Another way to run the omniprogram is by having Python installed on your machine and downloading all Python files of the omniprogram. 
Then you just double-click the ```omniprogramGUI.py``` file which runs the GUI via the Python interpretor. This approach is more universal than approach 1, 
but maybe slower and requires your system to have Python but it is the path to having the most recent version of the Omniprogram and it will work on more than just Windows.

### 3. The Interpreted Version but Segmented
The most wacky way to run this is by downloading just a specific segment and all named programs matching. In other words, you could download ```aPrograms.py``` and all the Python files associated with ```aPrograms.py```
as well as the needed library files and run just that alphabetical category of omniprograms. Why you would do this is beyond me, 
since the Omniprogram is meant to interlock and work together and not be split up, but it's technically a way to run it.

### 4. The Interpreted Version but Extremely Segmented
If you want just one program from the Omniprogram and nothing else, you can download that specific Python file 
and any library Omniprogram files it depends on and just use Python to run that specific program. 
Again, this is cursed and yucky but technically valid.

### 5. Executables but You do it Yourself
This way involves having Pyinstaller installed on your system via pip and using it to compile specific omniprograms or the entire thing if the main EXE is a little dated.
This way would allow you to make exe's of the Omniprogram or parts of it for unix based systems potentially. This approach is messy but is technically valid also.

Of the five apporoaches approach 1 or 2 are your best bets but the other approaches work if you're feeling adventerous.

## Navigating the Program
When you first boot up the Omniprogram you see a menu with a quit button on top and a series of buttons labeled like: _ Programs. With _ being an alphabetical character.
This is done to alphabetically organize the programs to make them easier to find.

When you click on one of the alphabet buttons another window opens up with a quit button and a series of program names. These program names directly launch programs.
For example: clicking on A Programs launches a window titled "Programs That Start With A" which contains buttons for programs: ```Age Calculator```, ```Actillion FTL Calculator```, ```A Lunisolar Calendar```, ```Alien Name Generator```, ```Analog Clock```, and ```Astrology Zodiac Clock```. Clicking on Age Calculator would then launch the age calculation program. Quit quits any window. Multiple programs of the Omniprogram can be open at the same time.

That's generally how to navitage the Omniprogram.

## Omniprogram Contents

What will be listed is all the programs the Omniprogram contains as well as a brief description for each one. 
These programs are inherently alphabetized via how the main menu is setup. 

### A Note on Input Fields
Basically every input field uses a custom library to parse input. As a result if garbage is given, a default value is assumed, typically 0 or 1.
As a result many programs when given bad input somewhere will instead put in a default value rather than error out. 
It's more slick but could lead to some confusion when using these programs.

### A Programs
This program contains all programs that start with the letter A.

#### Age Calculator
Calculates the age based on the input birth date and input current date. 
If the birth date is after the current date, then it acts like a countdown with the age being negative. 
It's best to have the start date be before the current date to minimize confusion.

#### Actillion FTL Calculator
Converts between a multiple of light speed and an Actillion FTL Factor (a fictional species' metric for speed).
One input field prompts for a C multiple, which is converted to the equivalent Actillion FTL Factor when the conversion button is pressed. 
The opposite happens in the second input field, where an Actillion FTL Factor is translated to a lightspeed multiple.

#### A Lunisolar Calendar
Takes in an input date and converts it to a custom made luni-solar calendar that contains 12 to 13 months in a year with the months being synched up with the moon.

#### Alien Name Generator
When the button is pressed, the program generates a random alien name based on three randomly picked chunks.

#### Analog Clock
A big fancy analog clock display that shows the time, date, day of the week, moonphase, 
and changes color depending on the time of day.

#### Astrological Zodiac Clock
Displays the current position in the zodiac cycle according to Astrology. The moonphase is also displayed and the stars 
in the background between the zodiac wheel and the moon are randomly generated each time the program is opened.
Generally, it's just a fancy zodiac clock for those who believe in that sort of thing.

### B Programs
Launches all programs that start with the letter B.

#### 