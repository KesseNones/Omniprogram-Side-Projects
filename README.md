# Omniprogram Side Projects
Created By Jesse A. Jones
## Introduction
The Omniprogram is a collection of dozens of converters 
and other random tools I felt were useful to make for myself.
This program has been assembled over the course of years of messing around with Python, 
first in terminal format programs and then in GUI form after learning about tkinter.
This repositorty is a compilation of all such programs as well as an executable version to run on windows.

THIS DOCUMENTATION IS A WORK IN PROGRESS SO LIKELY WILL HAVE SPELLING AND OTHER ERRORS. IGNORE THOSE BECAUSE
THEY WILL GET FIXED IN TIME.

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

### K Programs

#### Kardashev Calc
Converts a civilization's power consumption in Watts to a Kardashev scale number 
based on Sagan's formula or converts a Kardashev Scale tier to power consumption.

#### Kesse Nones Alias Generator
Randomly generates an alias for Kesse Nones by swapping 
out the first letter of each name chunk to another letter or nothing.
Why does this exist? Don't worry about it.

### M Programs

#### Metric Date
Displays the current live metric date expressed as kilodays.
As you'd guess, one kiloday is 1 000 days.
Metric date 0 is 12000 years ago when humans began agriculture.

#### Metric Date Calculator
Calculates metric date based on input date and time.

#### Metric Stopwatch
A stopwatch that can be used as a, well, stopwatch.
It counts up time as a measure of milidays, or thousandths of days.
One miliday is 86.4 seconds or about one and a half minutes.
The first three decimals to the right of milidays would therefore be microdays 
and the further right three decimals would be nanodays.
This stopwatch can be operated using three buttons: ```Start```, ```Pause```, and ```Reset```.
```Start``` Starts or resumes the stopwatch time. ```Pause``` pauses the stopwatch or does nothing it it's already paused.
Lastly, ```Reset``` resets the stopwatch to time 0.

#### Metric Countdown
Gives a metric countdown based on an input date and time. The countdown can count down or up depending 
on if the given date and time is in the future or the past reletive to the current system time it uses as a basis.
The countdown is given in units of days with precision out to microdays.

#### Moon Phase Calculator MK II
Calculates the moon phase and moon age based on an input date and time.

#### Magic Eight Ball
Mimics the iconic Magic Eight Ball toy. You use it by asking it a question mentally 
or verbally (or not it's up to you) and pressing the ask button to get an answer.
A random answer is then given based on all possible responses of the real Magic Eight Ball toy.
##### NOTE
Like with the Connect Four game, the executable's sound is broken.
However, if you use the interpreted version of the Omniprogram then 
each generated response will have a cheesy voice line if sound is enabled.

#### Minecraft Calendar Calc
Given an input date, calculates the date in the Minecraft calendar I made up for a country.
It consists of a year with 12 months of 8 days each, making a 96 day year.
The months are: ```Silverfish```, ```Cow```, ```Ocelot```, ```Rabbit```, ```Ender```, ```Skeleton```, 
```Horse```, ```Sheep```, ```Steve```, ```Chicken```, ```Wolf```, ```Pig```.
The month names are based on the Chinese Zodiac but changed to Minecraft mobs and stuff.
For comparison, the chinese zodiac animals are: ```Rat```, ```Ox```, ```Tiger```, ```Rabbit```, 
```Dragon```, ```Snake```, ```Horse```, ```Goat```, ```Monkey```, ```Rooster```, ```Dog```, ```Pig```.

#### Mayan Long Count Calendar Calc
Given input date, calculates date in Mayan time systems.
Displays date of Mayan Long Count, Tzolkin, Haab, and current Lord of the Night.
2012-12-20 is: Long Count -> 0.0.0.0.12.19.19.17.19, Tzolkin -> 3 Cauac, Haab -> 2 Kankin, and Lord of Night -> G8
2012-12-21 is: Long Count -> 0.0.0.0.13.0.0.0.0, Tzolkin -> 4 Ahau, Haab -> 3 Kankin, and Lord of Night -> G9
This flip over was a big deal and was cool to happen. However, it wasn't foretold as the end of the world like myths of the time (late 2000s to early 2010s) would have you believe.

#### Maker of Nines
This is a crappy Cookie Clicker bootleg idle game that involves making more and more Nines.
What are Nines? That would take too long to explain. Anyways, you can click on the Nine to make Nines
manually which can then buy upgrades like in the game Cookie Clicker. 
This game has a save/load mechanic to save your data. It also autosaves every few minutes or so.
It generates a text file with some save data named ```nineSave.txt```. If you try to load the save
that doesn't exist, an erorr is thrown in the terminal but it keeps working. You just have to have it save
that file. So yeah, a crappy idle game is basically what this is.

#### Metric Date to Normal Date
Takes in an input metric date expressed as kilodays and converts it to the equivalent calendar date.

### R Programs

#### Reformed Calendar Calculator
Takes in an input date and calculates the Reformed Calendar date from it.
The Reformed Calendar is a calendar of thirteen 28 day long periods called 
Quads. A 14th Quad is at the end of the year and usually just contains 1 day
sometimes 2. This totals to 365/366 days for a the whole year.

The calendar also displays an Age, which is useful for long term time keeping.
One age is 10 000 years. It started with the 0th Age and went up from there,
so being the first age means the year is 10 000 plus 2023 (more if you're from the future) of the current age.


#### Roman Numeral Converter
Takes in an integer and converts it to an equivalent Roman Numeral. 
This system uses a bar system for numbers greater than 3 999. 
For instance, 3 999 is MMMCMXCIX and 4 000 is |IV| which means 4 times 1000.
So, to express say, a million you do |M| which is 1000 times 1000.
A billion would be ||M||, a trillion |||M|||, a quadrillion, |>M|>k, a quintillion >M>, etc.
Basically the side bars mimic roman numerals in how they progress too, 
just each bar number equates to another multiplication of a thousand.
In the converted number, numbers with bars on the sides are surrounded by parenthesis too to make seperating the large numbers possible.
For example a million reads as ```(|M|)```.

#### Relativity Calculator
Given a distance and velocity, it calculates how long it takes to get there from the traveler's perspective.
This program can have a unit specifier of ly in distance and a light speed percentage symbol % in velocity.
For example you can input the distance as ```11.9 ly``` and the speed as ```92 %``` and it will understand you mean
traveling 11.9 light years with the velocity of 92 percent light speed. 
It then gives the number of seconds and standard formatted time to travel that distance from the traveler's perspective.

#### Roman Numeral Clock and Calendar
Displays the current date and time in Roman Numerals

#### Reformed Calendar Live Edition
Displays the current calendar page of the current date of the Reformed Calendar.
It's layed out like a calendar page would be in a grid pattern of days.

The weekdays are different of course since it's a different calendar.
The names of the week days are: ```Solday```, ```Hermesday```, ```Venusday```, 
```Terraday```, ```Lunaday```, ```Marsday```, ```Joviday```.
Translated to more plain english the week days are: ```Sun Day```, ```Mercury Day```, ```Venus Day```, 
```Earth Day```, ```Moon Day```, ```Mars Day```, ```Jupiter Day```

The medium periods of this calendar are called Quads, short for Quadroons. A quad is a period of four weeks in this calendar.
There are 13 quads of the main calendar and one really short extra quad to complete the year at the end.
The names of the quads are basically a number in latin/spanish and some random suffix, except for the last one which literally just means extra.
The Quads are: ```Unuary```, ```Duotober```, ```Tres```, ```Quadtober```, ```Quintecember```, ```Sixril```, 
```Septecember```, ```Octo```, ```Novembuary```, ```Decemptober```, ```Undecimber```, ```Dosdecimber```, ```Tridecimber```, and ```Supplementary```

The current day in the Quad is highlighted yellow. Days already complete if any are a dark grey.
Future days if any are a light grey. Beyond the days of the Quad, the Quad name is also displayed as well as the year and Age.

#### Reformed Calendar Calculator Mk II
Looks like the Reformed Calendar Page described above and starts on today's date in the calendar but can take in an input Gregorian Calendar date.
This input Gregorian Calendar date is then converted to the Reformed Calendar and the calendar page is remade to display the calculated date.

### S Programs

#### Stardate
Displays a version of the Stardate from Star Trek the Next Generation.
The Stardate precision can be controlled by the precision slider 
from the classic one decimal of precision all the way up to 5.

#### Stardate Calculator
Takes in an input date and time and calculates the 
Star Trek TNG Stardate, displaying it at five decimals of precission.

#### Season Calendar Calculator
Takes an input date and calculates the Season Calendar date. 
This calendar displays the day of the current season, the season, 
and the year which is the gregorian year minus 2000.
It also shows the moonphase of that day, for fun.
If you're from the southern hemisphere, just flip the season it says it is.
It's a very Northern Hemisphere biased calendar.

#### Shire Calendar Calculator
Receives an input date and calculates the date in the Shire Calendar of Middle Earth.
It's similar to the Gregorian Calendar but with some more flavor.

#### Second Counting Stopwatch
A stopwatch that counts up in the units of seconds from 0.
This stopwatch is basically a stopwatch without converting seconds 
to other time units and just keeping with seconds.

Three buttons control this stopwatch: ```Start```, ```Pause```, and ```Reset```.
The ```Start``` button starts or resumes the stopwatch, the ```Pause``` button pauses the stopwatch 
or does nothing if the stopwatch is already paused (CURRENTLY PRESSING PAUSE MORE THAN ONCE ACTUALLY MESSES WITH IT. WILL GET FIXED SOON).
```Reset``` resets the stopwatch time to 0 from wherever.

#### String Reverser
Takes in a string as input and reverses it, displaying the result in the bottom box. 
Pretty simple.

#### Seconds in Day
Counts up the number of seconds elapsed in the current day based on local system time.

#### Season Clock
A clock face that displays where in the seasonal cycle the Northern Hemisphere is by having
a clock hand pointing to the portion of the season it is. It's very pretty.
Again this is Northern Hemisphere biased, if you're from the Southern Hemisphere, just flip the seasons, 
so Winter becomes Summer and Autumn becomes Spring. 

It also displays the moon phase because why not.

#### Starfield
Displays a starfield that moves stars by you as if you were traveling at slow warp speed.
It looks like you're traveling through space. The inner layer keeps spawning new stars and moving.
The background stars eventually disappear as they move past you. Generally it's just a neatish 
looking starfield made of randomly generated "stars".

#### Seasonaly Synced Calendar
Takes an input date and calculates the equivalent date in the Seasonaly Synced Calendar.
This calendar is like our own but more in sync with the seasons, as the name indicates.
The calendar takes the current date, moves it back 19 days 
and the year starts in March instead of January. 

As a result of these adjustments, 
based on the Northern Hemisphere, the year starts on the spring equinox 
which reads as March 1st which is March 20th in our calendar. Then, three months later, June is reached and marks the start 
of Summer at June 1st which is June 20th in our calendar. Granted the Summer Solstice is June 21st but it's close enough, much closer than our current calendar.
Three months after that Autumn begins on September 1st which is September 20th in our calendar usually. This is close enough to the equinox to work.
Three months after that begins the final season of Winter on December 1st, December 20th in our calendar.

Beyond just having the seasons starting at the start of months, each season now contains exactly 3 months: Spring has March, April, and May, 
Summer has June, July, and August, Autumn has September, October, and November, and Winter has December, January, and February. 
Since February is the last month of the year in this calendar, the leap day is at the end of the year instead of at an arbitrary early point 
of the year. Starting in spring also just makes more sense since it signifies a time of rebirth and all that.

Another neat bonus is that some of the month names actually make sense again. Here are the months with their new numbers: <br>
```
1. March 
2. April 
3. May 
4. June 
5. July 
6. August 
7. September
8. October
9. November
10. December
11. January
12. February 
```
Notice how September, meaning seventh month, is now actually the seventh month, 
just like how october is the 8th, november is the 9th and december the 10th. 

Overall, no one will ever use this calendar because switching would be confusion 
and the pain of switching far outweighs any benefits this calendar provides. Still a neat adjustment though.

### T Programs

#### Temp Converter
Converts an input temperature between the three main temperature systems of Celsius, Fahrenheit, and Kelvin
and outputs the converted temperature.

#### Time Displayer Ultima
Displays a series of previously made time systems live.
The systems displayed are the Metric Date, Star Trek Next Generation Stardate,
Star Trek The Original Series Stardate, UTC Time, Local Time, the current date in the Gregorian and Seasonal Calendar, the week number of the year, the day number of the year, the Moon Age, and the Moonphase.

#### TOS Stardate
Displays the live Star Trek the Original Series Stardate with precision range of one decimal to 5 decimals.

#### TOS Stardate Calc
Takes in an input date and time and calculates the Star Trek: The Original Series Stardate based on the input.

#### TNG True Stardate
Displays another version of the live Star Trek: The Next Generation Stardate which accounts for the current
year instead of being the show stardate continued like the other TNG Stardate.
This version of the stardate involves calculating how many years displacement from 2323 for the first digit segment and the fragment of the year for the last four digits.

#### TNG True Stardate Calculator
Takes in an input date and time and calculates the True TNG Stardate based on the input.