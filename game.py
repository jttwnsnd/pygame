import sys #we will need sys so the user can quit
import pygame #DUH
from hero import Hero #bring in the class  with all its methods and glory

#set up the main core function
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1000,800)) #set screen size
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	bg_color = (82,111,53)
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	while 1: #run this loop forever...
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		hero.draw_me()#draw the hero
		pygame.display.flip()

run_game() # start the game