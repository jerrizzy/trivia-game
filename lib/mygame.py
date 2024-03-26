import pygame
from sys import exit
from random import randint


def display_score():
    current_time = current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time) # Ensure current_time doesn't go below 0
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

start_time = 60 # Set the initial time to 60 seconds

pygame.init() # this function starts pygame. like starting a car with a key
screen = pygame.display.set_mode((800, 600)) # this is our (display surface). Point of origin 
#The window our player sees. first number is width, sencond one 
#is height of the window. set_mode function takes at least 1 argument, in this case a tuple

pygame.display.set_caption('Blade')# it names the game on the window
clock = pygame.time.Clock() #Clock object keeps track of time and control frame rate. Here it does nothing, it's being called in the while loop
test_font = pygame.font.Font('lib/font/Pixeltype.ttf', 50) #this works with our variable text_surface. It determines the kind of font, and size

test_surface = pygame.Surface((100, 100)) # tuple is the size of item = 100px by 100px
test_surface.fill('Red')
test_rect = test_surface.get_rect(midbottom = (400,250)) #get_rect is rectangle to contain the item so that it can be controlled. x,y axis position: 400px to the left by 200px from the top.



while True:
    screen.fill(('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# this quits the game
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print('MOUE UP')

    screen.blit(test_surface, test_rect) #blit grabs the rectangle drawn around the surface from (midbottom) point, and depends the point being grabbed, it positions the surface on x,y axis position: 400px to the left by 200px from the top
    test_rect.x += 5
    if test_rect.right >= 950: test_rect.left = 0

    mouse_pos = pygame.mouse.get_pos()
    if test_rect.collidepoint(mouse_pos):
        print('collision')

    display_score()
    pygame.display.update()
    clock.tick(60)