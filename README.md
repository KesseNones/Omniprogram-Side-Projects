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
Displays the time in base six, with there being 40<sub>6</sub> or 24<sub>10</sub> hours in the day and then the hours being divided into 100000<sub>6</sub> or 7776<sub>10</sub> fractional components.

#### Base Calculator
Performs addition, subtraction, multiplication, and division in bases 2 to 36. It generally can 
do some decimal stuff but its floating point handling is pretty jank so best to avoid too much of it.
Generally it's a basic calculator that can to base 2 to 36.
##### NOTE:
Due to how this calculator works input parsing is not very good. It accounts for empty input but otherwise it errors out if the input is any other kind of bad.

#### Base Six Clock V. II
Displays the time of day but in a true base six fashion. It displays first 216<sub>10</sub>ths 1000<sub>6</sub>ths of the day which is then followed by 
a point that displays 216<sub>10</sub>ths of 216<sub>10</sub>ths of the day or 1 000 000<sub>6</sub>ths (46 656<sub>10</sub>ths) of a day.

### C Programs

#### Coin Flipper
Pretty self explanitory. You click the button, it displays a flipping message, and then displays the result of the current coin flip.

#### C to Warp Converter
You input a multiple of the speed of light and it converts it to a version of the Star Trek The Next Generation Warp Factor. 
Essentially it raises the input speed of light multiple to 3/10 and if the multiple is greater than 1516 C 
then it uses a complicated log based algorithim to calculate the threshold warp factor ranging from warp 9 to warp almost 10.
If infinity or a float large enough to register as infinity is inputted then warp 10 will result since warp 10 is infinite velocity.

#### Connect Four
This program plays a game of Connect Four against an "AI". This was made for a school project in Fall Semester 2020.
Essentially it follows the rules of Connect Four. You make a move and then the AI makes a move. 
You can control how much the AI thinks by moving the AI difficulty slider in a range of 0 to 7. 

##### Note 
Past the difficulty of 5, the AI really starts to slow down because of deep recursion. 
Difficulty 7 is easily the slowest but the AI is hardest to fight on this level. 

##### Tiles
The tiles of the board are circles representing where the pieces would be on an actual board. 
White circles represent nothing there. Red is player pieces, and black is AI pieces.
The tiles fall in an animated manner to look cooler. When a game is won for the player or AI, 
a blue line is drawn to indicate what won the game for the player/AI.

##### Message Text
Below the board is a line of text that displays crucial game information.
When the game boots up or a new game is started it prompts the user to click where they want to move.
After the user makes their move, the AI makes its move 
and then the text displays what column number it moved in range 0 to 6.
If the player wins the game it says so, if the AI wins it says so.
If the column is full it's indicated. If a replay is happening it says so.
If the AI is taking a while you can see it say ```Loading...```.
Generally this text just indicates useful game information.

##### Buttons
###### New Game
Starts a new game, clearing the game data.

###### Quit
Quits the program.

###### Replay Game
When clicked the game runs from the beginning to the current game state. 
Useful for showing a really close game or what exactly happened.

###### Sound On/Off
Enables or disables sound. 
CURRENTLY SOUND IN THE EXECUTABLE VERSION OF THIS IS BROKEN SO SOUND DOESN'T WORK THERE.
Assuming sound does work because you're running the interpreted version of the Omniprogram with all files present, 
then some goofy sound effects play if enabled like: piece placement sound, player victory sound, AI victory sound, and
Stalemate sound.

#### Chinese Year Calculator
Given an input year the Chinese Zodiac equivalent is calculated. 
The output indicates the zodiac animal, element, yin/yang, as well as year of cycle and cycle number.

#### Calculate Weighted Grade
An old non-GUI program that can calculate a grade given percentage category weights and how much you have in each sub-category.
For instance, if you have a great with 50 percent exams and 50 percent 
homework where you have 90 percent on homework and 70 percent on exams the calculated class grade would be an 80 %.
It asks if you're finished a lot because it's not a GUI. Also quitting this program exits the entire Omniprogram.
Honeslty this program kinda sucks and probably will be removed in the future. Plus, there's a GUI version that works much better.
##### NOTE
THIS IS AN OUTDATED CODE VERSION KEPT AROUND FOR LEGACY PURPOSES. IT'S NOT A GUI.

#### Calendar Month Displayer
Given an input year and month the calendar page for that month of that year is displayed.
It works but it's a bit janky. It may be fixed one day.

#### Caesar Cipher
Takes in a string and shifts each alphabetical character forward or backwards by 0 to 25 characters,
encoding/decoding it in the manner of the Caesar Cipher.

#### Centaurian Time
Displays the current time at m.i.b headquarters which uses a 37 hour day. You get used to it, or you have a psychotic episode.

#### Calculate Weighted Grade GUI Edition
Used to calculate a grade you'd have in a class based on what 
categories it has and what percentage you have in each category.
To add a category you push the ```Add Entry``` button which pushes on a new entry
that has fields for the category value and your percentage in it.
To remove an entry you use the ```Pop Last``` button which removes the most recently added category.
To calculate the grade you just press the ```Calculate Grade``` button which calculates the grade
based on input information and spits out a percentage and letter grade.
If no entries exist, nothing happens when ```Calculate Grade``` is pressed.

### D Programs

#### DST Calendar Converter
Given an input day, a calendar date is calculated for Don't Stare's world. 
This only works if the time in the world is set to its default parameters and isn't messed with.

#### Day Difference Date Calc
Calculates the date given a day offset from today's date. 
If the offset given is invalid input or 0, then today's date is given back.
Otherwise the date is calculated based on the offset positive or negative given.

#### DST Rough Nightmare Cycle Calculator
This was an attempt to be able to calculate the rough phase of the nightmare cycle in DST's caves. 
It didn't work so it was abandoned. It didn't work meaning the code works and everything but the 
nightmare phase given is basically always wrong.

#### Different Countdown Clock
Given an input date and time, generates a countdown to or from a date.
The units presented in the countdown are years, weeks, days, hours, minutes, and seconds, in that order.

#### Different Clock (Not Mine)
Displays the time based on a goofy clock reform idea I saw on YouTube.
A day has 20 hours with each hour having 20 minutes, making each minute 216 seconds.

#### 360 Degree Clock
Shows the time in a degree-centric format, with the day being made of 360 degrees 
with each degree having 60 arc-minutes and each arc-minute having 60 arc-seconds.

### E Programs

#### Eight Day Portion Clock
Displays the current time if the day were broken up into eight chunks instead of two.
Instead of just AM and PM, the chunks are: Late Night, Early Morning, Morning,
Late Morning, Afternoon, Late Afternoon, Evening, and Night. 
The clock displays the time ranging from 1 to 3 o'clock with minutes and seconds working as expected, 
and the day portion name displayed below that.

#### Eight Day Portion Clock Calculator
Takes in an input time and converts it to the previously 
discussed eight day portion clock, displaying it below.

#### Easter Calculator
Given an input year, calculates the date of Easter for that year.
It's pretty accurate only occasionally being off by maybe a week.

#### Eru'varian Clock
Displays the current universal time on the planet Eru'var. 
The time on Eru'var involves dividing the day into 12 hours
and each hour into base 12 decimal chunks up to four places.
This is done because the Eru'varians had 12 fingers and toes
so they used base 12.

#### Eru'varian Calendar and Clock
Displays the current Eru'varian time and date.
The date is all displayed in base 12 because the Eru'varians used base 12.
You have the year, lunar cycle, day, and day of the week. A year contains 12 lunar cycles of 30 days each.
An Eru'varian week is 6 days long with weekdays named: ```Torfung```, ```Solfung```, ```Varfung```, ```Melfung```, ```Orivfung```, and ```T'rarfung```. 
Translated these weekdays mean: 
Sun day, Moon Day, World Day, Melron's Day (Day of the First Monarch), Oriv's Day, and T'rar's Day. You also have the sub-age which is a period
of 10 000<sub>12</sub> (20 736<sub>10</sub>) Eru'varian years. Each Eru'varian year
is about 1.009 Earth years. Explaining the whole "Age of Balance" thing would
take a while because it's wacky lore of my own universe.

#### Eru'varian Reckoning Calculator
Given an input date and time, the program calculates the equivalent Eru'varian date and time.

#### Elven Calendar Calculator
Given an input date, calculates the current date in the Elven Calendar of Middle Earth.

#### Eridian Clock
A base six time system used by the Eridians of the Project Hail Mary universe. One day is 7 776 Eridian Seconds.
Each Eridian Second is 2.667 Earth seconds so one day is 20 738.6 Earth seconds, or about 5.8 Earth hours.

### H Programs

#### Huge Number Converter
Given an input of a number that may be massive, it converts the number 
to scientific notation and also gives the name of the number.

#### Hexadecimal Encoder
Takes in a string and converts it to Unicode Hexadecimals, or vice versa.

#### Hexadecimal Clock
Counts the number of fractions in a day in base 16. There are 10 000<sub>16</sub> or 65536<sub>10</sub> 
fractional chunks in the day. It counts from 0000<sub>16</sub> to FFFF<sub>16</sub> and then overflows.

