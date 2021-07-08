import pygame
import csv

#Setting up Pygame
pygame.init()
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Alex's Game")
framerate=10 #how many times the main loop should run in a second

#Returns a set from the csv with the name entered
def prepareCSV(filename):
	b = []
	with open(filename,newline="") as csvfile:
		a = csv.reader(csvfile)
		for row in a:
			b.append([int(x) for x in row])
	return(b)

def display_obstacle(lane,y):
	pygame.draw.rect(win,(100,100,100),((200*lane)-200,y,200,10))

#attributes for cursor
x = 200
y = 590
width = 200
height = 10

# configure controls
def quit_check():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True
def left_check(a):
	return a[pygame.K_LEFT]
def right_check(a):
	return a[pygame.K_RIGHT]
def activate_check(a):
	return a[pygame.K_SPACE]

#Beginning of the user seeing Stuff™
validInput = False
while not validInput:
	try:
		gameData = prepareCSV(input("What is the name of the game data file?\n> "))
		validInput=True
	except:
		print("INVALID FILE! Please try again.")
		validInput=False
print("Loading Game Data.")

# Creation of variables related to the level
rowCount=gameData[0][0] #Amount of rows in the level
rowPace=gameData[0][1] #Amount of rows per minute
startRow=1 #First row that hasn't come and gone yet
workingRow = 0 #Row that is being calculated
rowFrametime = framerate*60/rowPace #How many frames any one row will be on screen for
rowSpeed = rowFrametime//600 #How many pixels a row moves in a frame
frameRemainder = 0 #How many frames have passed since startRow has changed.
rowsVisible = rowSpeed

#main game loop
run = True
frameCounter = 0
while run:
	#makeshift clock in ms
	pygame.time.delay(1000//framerate)
	frameCounter+=1

	#check for quit
	if quit_check():
		run = False
		exit
	
	#set character position
	keys = pygame.key.get_pressed()
	if left_check(keys) and not right_check(keys):
		x = 0
	elif right_check(keys) and not left_check(keys):
		x = 400
	else:
		x = 200
	
	#Draw lanes
	pygame.draw.rect(win,(75,0,0),(0,0,200,600))
	pygame.draw.rect(win,(0,75,0),(200,0,200,600))
	pygame.draw.rect(win,(0,0,75),(400,0,200,600))

	#Draw character
	if not keys[pygame.K_SPACE]:
		pygame.draw.rect(win,(200,200,200),(x,y,width,height))
	else:
		pygame.draw.rect(win,(200,250,250),(x,y,width,height))

	#Should an obstacle be drawn?
	frameRemainder+=1
	if frameRemainder == rowFrametime:
		startRow+=1
	for rowPlus in range(startRow-1,rowPace-1): #number of rows visible given all rows are filled
		workingRow = startRow+rowPlus #the row in the list that is being looked at
		for lane in range(1,3):
			#Don't try to render rows after the last one
			if workingRow >= rowCount:
				run = False
				exit()
			if gameData[workingRow][lane-1] == 1:
				display_obstacle(lane,frameCounter*10)
	
	#Update screen
	pygame.display.update()

pygame.quit