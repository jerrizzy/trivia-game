import pygame
from sys import exit
from random import randint, choice



def display_score():
    current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time) # Ensure current_time doesn't go below 0
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    return current_time

start_time = 5 # Set the initial time to 60 seconds

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
box_rect = box_surface.get_rect(midbottom = (400,300)) #get_rect is rectangle to contain the item so that it can be controlled. x,y axis position: 400px from the left by 200px from the top.

box_surface1 = pygame.Surface((100, 100)) 
box_surface1.fill('Blue')
box_rect1 = box_surface1.get_rect(midbottom = (400,450))

box_surface2 = pygame.Surface((100, 100)) 
box_surface2.fill('Green')
box_rect2 = box_surface2.get_rect(midbottom = (400,600))

box_surface3 = pygame.Surface((100, 100)) 
box_surface3.fill('Yellow')
box_rect3 = box_surface3.get_rect(midbottom = (400,750))

#intro
box_intro = pygame.Surface((200, 200)) #size
box_intro.fill(choice([(0, 0, 255), (255, 0, 0), (255, 255, 0)])) #random color
box_intro_rect = box_intro.get_rect(midbottom = (400,400)) #position

title_surface = test_font.render('Space Trivia', False, (111, 196, 170))
title_rect = title_surface.get_rect(center = (400, 50)) #our screen is 800 by 400. half of 800 is 400 to get centered

title_message = test_font.render('Click the box to play', False, (111, 196, 170))
title_message_rect = title_message.get_rect(center = (400, 600))

box_gravity = 30

add_time = 5

game_active = False

while True:
    screen.fill(('white'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# this quits the game
            exit()

        if game_active:
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
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_intro_rect.collidepoint(event.pos):
                    game_active = True
                
    if game_active:       
        # box_gravity += 0.005 #this moves the box faster
        # box_rect.x += box_gravity
        screen.blit(box_surface, box_rect) #blit grabs the rectangle drawn around the itemm surface from (midbottom) point from when we created the rect, and depends the point being grabbed, it positions the surface on x,y axis position: 400px to the left by 200px from the top
        # box_rect.x += 10 #moves the box on x axis
        # Attempting to randomly move box in both X and Y
        box_rect.x += randint(-20, 20)
        box_rect.y += randint(-20, 20)
        if box_rect.right >= 950: box_rect.left = 0 #places box on other side of screen after the box goes beyond the screen. remember screen is 800px on x and y axis. so it waits till it disappears after 1000px then spawns it on the opposite side at 0px 
        elif box_rect.left <= 0: box_rect.right = 950
        elif box_rect.bottom >= 950: box_rect.top = 0
        elif box_rect.top <= 0: box_rect.bottom = 950

        screen.blit(box_surface1, box_rect1) 
        # box_rect1.x -= 5
        box_rect1.x += randint(-20, 20)
        box_rect1.y += randint(-20, 20)
        if box_rect1.left <= 0: box_rect1.right = 1000
        elif box_rect1.left <= 0: box_rect1.right = 1000
        elif box_rect1.bottom >= 1000: box_rect1.top = 0
        elif box_rect1.top <= 0: box_rect1.bottom = 1000

        screen.blit(box_surface2, box_rect2) 
        # box_rect2.x += 10
        box_rect2.x += randint(-20, 20)
        box_rect2.y += randint(-20, 20)
        if box_rect2.right >= 950: box_rect2.left = 0
        elif box_rect2.left <= 0: box_rect2.right = 950
        elif box_rect2.bottom >= 950: box_rect2.top = 0
        elif box_rect2.top <= 0: box_rect2.bottom = 950

        screen.blit(box_surface3, box_rect3) 
        # box_rect3.x -= 5
        box_rect3.x += randint(-20, 20)
        box_rect3.y += randint(-20, 20)
        if box_rect3.left <= 0: box_rect3.right = 1000
        elif box_rect3.left <= 0: box_rect3.right = 1000
        elif box_rect3.bottom >= 1000: box_rect3.top = 0
        elif box_rect3.top <= 0: box_rect3.bottom = 1000
        

        # mouse_pos = pygame.mouse.get_pos()
        # if box_rect.collidepoint(mouse_pos):
        #     print('collision')

        display_score()
        if display_score() == 0:
            game_active = False
    else:
        screen.fill('Red')
        screen.blit(box_intro, box_intro_rect)
        screen.blit(title_surface, title_rect)
        screen.blit(title_message, title_message_rect)
        


    pygame.display.update()
    clock.tick(60)