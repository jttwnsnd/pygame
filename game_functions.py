#we will put all main game functions here
import sys, pygame

def check_events(hero):
	for event in pygame.event.get(): #run through all events
			if event.type == pygame.QUIT: #if the events is quit...
				sys.exit()
			elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down.
				if event.key == pygame.K_RIGHT:
					hero.rect.centerx += 5#move the character to the right per press
				elif event.key == pygame.K_LEFT:
					hero.rect.centerx -= 5#move the character to the left per press
				elif event.key == pygame.K_UP:
					hero.rect.centery -= 5
				elif event.key == pygame.K_DOWN:
					hero.rect.centery += 5
			#273 = up
			#275 = right
			#274 = down
			#276 = left
#handle all the screen updates and drawing
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color)
	hero.draw_me()#draw the hero
	pygame.display.flip()