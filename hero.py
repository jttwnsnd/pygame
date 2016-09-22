import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen.
		# load the hero image, get it's rect
		self.image = pygame.image.load('ball.gif')
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object on any object
		self.screen_rect = screen.get_rect() #assign a var so the hero knows how big the screen is.
		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen.
		self.rect.bottom = self.screen_rect.bottom #this will put our hero 'bottom' at the bottom of the screen.

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect) #draw the surface..(the image, the where)