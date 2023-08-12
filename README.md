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

#### Bearimy Converter
Either takes in an amount of time elapsed to convert to Jeremy Bearimies or takes in Jeremy Bearimies and gives back time elapsed. 
Jeremy Bearimies are from the show "The Good Place" which is a fun wacky show.

#### Base Converter
Takes in an integer in base range 2 to 36 and converts it to base 10 (decimal) and displays the result.
Also can take in a base ten integer and convert it to a number in base 2 to 36.
##### NOTE:
This converter has limited input parsing due to its nature so it will error out if invalid input beyond just a blank entry is given!

#### Binary Encoder and Decoder
Takes in a string and converts it to Unicode Binary or takes in a Unicode Binary string and converts it back to a regular string.
This program also has limited input parsing due to its nature.

#### Binary Clock
Displays the time of day in a truly binary format. The time is displayed in four blocks of four bits. 
Each bit represents a fraction of the day. The leftmost bit is a half 
of a day, the bit to the right of that is a quarter of a day, the one to the right of that an eighth of a day and onwards.
As a result, going from 11:59 to noon looks like: ```0111 1111 1111 1111``` to ```1000 0000 0000 0000``` 
and flipping to midnight looks like: ```1111 1111 1111 1111``` -> ```0000 0000 0000 0000```. 
The time itself is based on the system's local time.

#### Base Stopwatch
Acts like a stopwatch but can count up in different bases ranging from 2 to 36. 
Up to five places of precision can be displayed using the slider. As you'd expect of a stopwatch, it can be started, stopped, and reset.

#### Base Six Clock
Displays the time in base six, with there being 40~6~ or 24~10~ hours in the day and then the hours being divided into 100000~6~ or 7776~10~ fractional components.

#### Base Calculator
Performs addition, subtraction, multiplication, and division in bases 2 to 36. It generally can 
do some decimal stuff but its floating point handling is pretty jank so best to avoid too much of it.
Generally it's a basic calculator that can to base 2 to 36.
##### NOTE:
Due to how this calculator works input parsing is not very good. It accounts for empty input but otherwise it errors out if the input is any other kind of bad.

#### Base Six Clock V. II
Displays the time of day but in a true base six fashion. It displays first 216ths 1000~6~ths of the day which is then followed by 
a point that displays 216ths of 216ths of the day or 1 000 000~6~ths (46 656~10~ths) of a day.

### C Programs
X 