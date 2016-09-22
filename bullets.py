import pygame #duh
from pygame.sprite import Sprite 

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings):
		#in game_settings
		# self.bullet_speed = 1
		# self.bullet_width = 3 #in px
		# self.bullet_height = 10
		# self.bullet_color = 90,90,90
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height) #make a bullet
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		self.y = self.rect.y

	def update(self):
		self.y -= self.speed #change the y each time the update is run by bullet_speed
		self.rect.y = self.y #update rect.position

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)