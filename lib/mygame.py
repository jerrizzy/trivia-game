import pygame
from sys import exit
from random import randint


def display_score():
    current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time) # Ensure current_time doesn't go below 0
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    return current_time

start_time = 30 # Set the initial time to 60 seconds

pygame.init() # this function starts pygame. like starting a car with a key
screen = pygame.display.set_mode((800, 800)) # this is our (display surface). Point of origin 
#The window our player sees. first number is width, sencond one 
#is height of the window. set_mode function takes at least 1 argument, in this case a tuple

pygame.display.set_caption('Blade')# it names the game on the window
clock = pygame.time.Clock() #Clock object keeps track of time and control frame rate. Here it does nothing, it's being called in the while loop
test_font = pygame.font.Font('lib/font/Pixeltype.ttf', 50) #this works with our variable text_surface. It determines the kind of font, and size

# boxes
box_surface = pygame.Surface((100, 100)) # this creates item. tuple is the size of item = 100px by 100px
box_surface.fill('Red') #gives item color
box_rect = box_surface.get_rect(midbottom = (400,250)) #get_rect is rectangle to contain the item so that it can be controlled. x,y axis position: 400px to the left by 200px from the top.

box_surface1 = pygame.Surface((100, 100)) 
box_surface1.fill('Blue')
box_rect1 = box_surface1.get_rect(midbottom = (400,370))

box_surface2 = pygame.Surface((100, 100)) 
box_surface2.fill('Green')
box_rect2 = box_surface2.get_rect(midbottom = (400,490))

box_surface3 = pygame.Surface((100, 100)) 
box_surface3.fill('Yellow')
box_rect3 = box_surface3.get_rect(midbottom = (400,610))

box_gravity = 0

add_time = 5

game_acive = True

while True:
    screen.fill(('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# this quits the game
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                print('collision')
                start_time += add_time # adds time when box is clicked
                # add move on to the next question code

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect1.collidepoint(event.pos):
                print('collision')
                start_time -= add_time # decrease time when box is clicked
                # add move on to the next question code

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect2.collidepoint(event.pos):
                print('collision') #clicking on this box neither increase or decrease time
                # add move on to the next question code

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect3.collidepoint(event.pos):
                print('collision')
                start_time = 0 # kills the time when box is clicked
                # add move on to the next question code
                
    if game_acive:       
        # box_gravity += 0.005 #this moves the box faster
        # box_rect.x += box_gravity
        screen.blit(box_surface, box_rect) #blit grabs the rectangle drawn around the itemm surface from (midbottom) point from when we created the rect, and depends the point being grabbed, it positions the surface on x,y axis position: 400px to the left by 200px from the top
        box_rect.x += 10
        if box_rect.right >= 1000: box_rect.left = 0

        screen.blit(box_surface1, box_rect1) 
        box_rect1.x -= 5
        if box_rect1.left <= 0: box_rect1.right = 1000

        screen.blit(box_surface2, box_rect2) 
        box_rect2.x += 10
        if box_rect2.right >= 1000: box_rect2.left = 0

        screen.blit(box_surface3, box_rect3) 
        box_rect3.x -= 5
        if box_rect3.left <= 0: box_rect3.right = 1000
        

        # mouse_pos = pygame.mouse.get_pos()
        # if box_rect.collidepoint(mouse_pos):
        #     print('collision')

        display_score()
        if display_score() == 0:
            game_acive = False
    else:
        screen.fill('Red')


    pygame.display.update()
    clock.tick(60)