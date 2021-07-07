import pygame
import csv

#Setting up Pygame
pygame.init()
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Alex's Game")

#Returns a set from the csv with the name entered
def prepareCSV(filename):
	b = []
	with open(filename,newline="") as csvfile:
		a = csv.reader(csvfile)
		for row in a:
			b.append(row)

#attributes for cursor
x = 200
y = 590
width = 200
height = 10

def quit_check():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

# configure controls
def left_check(a):
	return a[pygame.K_LEFT]
def right_check(a):
	return a[pygame.K_RIGHT]
def activate_check(a):
	return a[pygame.K_SPACE]

#main game loop
run = True
while run:
	#makeshift clock in ms
	#pygame.time.delay(1000//60)

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

	#Update screen
	pygame.display.update()
pygame.quit