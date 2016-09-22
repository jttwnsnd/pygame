#we will put all main game functions here
import sys, pygame
from bullets import Bullet #just call the class.

def check_events(hero, bullets, game_settings, screen):
	for event in pygame.event.get(): #run through all events
			if event.type == pygame.QUIT: #if the events is quit...
				sys.exit()
			elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down.
				if event.key == pygame.K_RIGHT:
					hero.moving_right = True #set the flag
				elif event.key == pygame.K_LEFT:
					hero.moving_left = True #set the flag
				elif event.key == pygame.K_UP:
					hero.moving_up = True
				elif event.key == pygame.K_DOWN:
					hero.moving_down = True
				elif event.key == pygame.K_SPACE:
					new_bullet = Bullet(screen, hero, game_settings)
					bullets.add(new_bullet)
			elif event.type == pygame.KEYUP: #user let go of a key
				if event.key == pygame.K_RIGHT:
					hero.moving_right = False
				elif event.key == pygame.K_LEFT:
					hero.moving_left = False
				elif event.key == pygame.K_UP:
					hero.moving_up = False
				elif event.key == pygame.K_DOWN:
					hero.moving_down = False

			#32 is space
			#273 = up
			#275 = right
			#274 = down
			#276 = left
#handle all the screen updates and drawing
def update_screen(settings, screen, hero, bullets):
	screen.fill(settings.bg_color)
	hero.draw_me()#draw the hero
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()