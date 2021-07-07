# ARealSeal/game

## What Needs to be Done

- [ ] Translate the CSV into obstacles
- [ ] Render obstacles
- [ ] Add CSV Support
- [ ] Collision Detection
- [ ] Score-keeping system

## How to Play

### Default Controls

- Left arrow to go into the left lane
- Right arrow to go into the right lane
- Space to activate

*You can change these in the main.py file under "# configure controls"*
Select the corresponding lane and activate at the right time to hit a target and get points.

## How to Create a Level

Levels are stored in a CSV document.
The first line contains the number of "frames" in the level, then the amount of frames a minute. Here's an example with 500 frames at 120 frames a minute:
*It also has a zero at the end, just ignore that part*

`500,120,0`

After that, each following line contains three numbers to indicate the status for the three lanes.
|Code|Description|
|---|---|
|0|Blank|
|1|Good object that the player wants to hit|
|2|Bad object that the player wants to avoid|
|3|good "hold" object|
|5|bad "hold" object|

## How the Program Works

1. The program sets up a Pygame window named `win` using pygame `method`s.
2. The terminal will query the user for the name of the file they want to use as the game's data using `input()`.
3. The program uses the library `csv` to parse the game data file into a `tuple` (representing the whole file) that contains more `tuple`s (representing each row) that contain each column.
4. The program declares `int` variables that specify the dimensions of the player's character. Coordinates in Pygame are relative to the top-leftmost corner of the screen.
5. The program defines functions that check for all the inputs that will be used to control the character. This is done so that it is easy to change the key layout.
6. The actual game part of the program all takes place in a giant `while` loop. This is done so that the game will continue until it reaches a reason to stop.
	- The program creates a `boolean` called `run` that will be checked to see if the game should continue.
	- If the program finds a reason to stop (the main one being the close button on the window being clicked), it will make `run` false, causing the `while` loop to become false.
7. The loop contains three distinct "parts:"
	- Checking to see what to do
		- Where should the character be?
		- What obstacles should be on the screen and where?
	- Checking the rules
		- Is there a collision between player and object?
		- Has the file ended?
		- Does the player die?
	- Drawing on the screen
		- First the background
		- Then the obstacles and character
		- `pygame.display.update()`
8. After the loop, the game displays the outcome of the play-through of the level.
