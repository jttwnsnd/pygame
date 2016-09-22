import pygame #DUH
from hero import Hero #bring in the class  with all its methods and glory
from settings import Settings
import game_functions as gf #an alias for game_functions
from pygame.sprite import Group

#set up the main core function
def run_game():
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(game_settings.screen_size) #set screen size
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	hero = Hero(screen) #set a variable equal to the class and pass it the screen
	bullets = Group() #set the bullets to group

	while 1: #run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen) #call gf, and get the check_event method
		hero.update() #update the flags
		bullets.update()
		gf.update_screen(game_settings, screen, hero, bullets) #call update_screen method.

run_game() # start the game