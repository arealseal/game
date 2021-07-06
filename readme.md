# ARealSeal/game

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
`500,120`
After that, each following line contains three numbers to indicate the status for the three lanes.
|Code|Description|
|---|---|
|0|Blank|
|1|Good object that the player wants to hit|
|2|Bad object that the player wants to avoid|
|3|good "hold" object|
|5|bad "hold" object|
