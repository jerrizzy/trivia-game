import pygame
from sys import exit
from random import randint, choice, shuffle
from question_class import Question
import copy
import time


shake_timer = time.time()

def display_score():
    current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time) # Ensure current_time doesn't go below 0
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (750, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    return current_time

# def resetgame():
#     global game_active, start_time
#     game_active = False
#     start_time = 5  # Reset start_time to its initial value


start_time = 60 # Set the initial time to 60 seconds

pygame.init() # this function starts pygame. like starting a car with a key
screen = pygame.display.set_mode((1500, 1000)) # this is our (display surface). Point of origin 
#The window our player sees. first number is width, sencond one 
#is height of the window. set_mode function takes at least 1 argument, in this case a tuple

pygame.display.set_caption('Blade')# it names the game on the window
clock = pygame.time.Clock() #Clock object keeps track of time and control frame rate. Here it does nothing, it's being called in the while loop
test_font = pygame.font.Font('lib/font/Pixeltype.ttf', 50) #this works with our variable text_surface. It determines the kind of font, and size
question_font = pygame.font.Font('lib/font/Pixeltype.ttf', 60)

intro_font = pygame.font.Font('lib/font/Pixeltype.ttf', 100)

#Question boxes
question_obj_list = Question.all_questions
copied_question_list = copy.deepcopy(question_obj_list)
shuffle(copied_question_list)
print(len(copied_question_list))

popped_obj = copied_question_list.pop()

print(len(copied_question_list))

q_text = popped_obj.question_text
answer = popped_obj.answers


def render_wrapped_text(text, font, color, box_width, box_height):
    # Start with the original font size
    # font_size = font.size()
    # print(font)
    text_surface = font.render(text, False, color)
    text_rect = text_surface.get_rect()

    # Check if the text exceeds the box width or height
    while text_rect.width > box_width or text_rect.height > box_height:
        # Reduce the font size
        # font_size += -1
        # NOTE: This font declaration line-of-code is a "land mine".
        #       Don't remove it or it'll blow up the script!
        font = pygame.font.Font('lib/font/Pixeltype.ttf', 16)

        # Render the text with the new font size
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()

    # Center the text within the box
    text_rect.center = (box_width // 2, box_height // 2)

    return text_surface, text_rect

# text_surface, text_rect = render_wrapped_text(answer[0], test_font, (111, 196, 170), box_surface.get_width(), box_surface.get_height())

# Blit the text surface onto the box surface
# box_surface.blit(text_surface, text_rect)

# boxes
box_surface = pygame.Surface((200, 200)) # this creates item. tuple is the size of item = 100px by 100px
box_surface.fill('Red') #gives item color
box_rect = box_surface.get_rect(midbottom = (750,300)) #get_rect is rectangle to contain the item so that it can be controlled. x,y axis position: 400px from the left by 200px from the top.

box_surface1 = pygame.Surface((200, 200)) 
box_surface1.fill('Blue')
box_rect1 = box_surface1.get_rect(midbottom = (750,550))

box_surface2 = pygame.Surface((200, 200)) 
box_surface2.fill('Green')
box_rect2 = box_surface2.get_rect(midbottom = (750,750))

box_surface3 = pygame.Surface((200, 200)) 
box_surface3.fill('Yellow')
box_rect3 = box_surface3.get_rect(midbottom = (750,900))

#intro
RED = (255, 0, 0)
radius = 20
box_intro = pygame.Surface((200, 200)) #size
box_intro.fill(choice(['#FF204E', "#070F2B", "#FC6736", "#FFD23F"])) #random color
box_intro_rect = box_intro.get_rect(midbottom = (750,500)) #position

title_surface = intro_font.render('Space Trivia', False, (111, 196, 170))
title_rect = title_surface.get_rect(center = (750, 100)) #our screen is 800 by 400. half of 800 is 400 to get centered

title_message = intro_font.render('Click the box to play', False, (111, 196, 170))
title_message_rect = title_message.get_rect(center = (750, 650))

intro_sound = pygame.mixer.Sound('lib/sound/dungeon_ambient_1.wav')

destroyer_sound = pygame.mixer.Sound('lib/sound/8bit_bomb_explosion.wav')
time_warp = pygame.mixer.Sound('lib/sound/space_shield.wav')
time_speed = pygame.mixer.Sound('lib/sound/button1.wav')
space = pygame.mixer.Sound('lib/sound/wind1.wav')

box_gravity = 30

add_time = 5
counter = 1 
game_active = False


while True:
    play_surface = pygame.image.load('lib/backdrop/space.png').convert()
    play_surface = pygame.transform.scale(play_surface, (1500, 1000))
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Blit the backdrop onto the screen
    screen.blit(play_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# this quits the game
            exit()

        if game_active and copied_question_list is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box_rect.collidepoint(event.pos):
                    print('collision')
                    correct_answer = answer[0]
                    time_speed.play()
                    start_time += add_time # adds time when box is clicked
                    # move on to the next question code
                    popped_obj = copied_question_list.pop()
                    q_text = popped_obj.question_text
                    answer = popped_obj.answers
                    counter += 1
                # NOTE: This else case was previously breaking our code by ensuring that
                #       if the player clicked anything besides the red box, the game 
                #       immediately resets because the `game_active` flag is immediately
                #       set to `False`.
                # else:
                    # game_active = False
                    # copied_question_list = copy.deepcopy(question_obj_list)
                    # shuffle(copied_question_list)
                    
                    
                if box_rect1.collidepoint(event.pos):
                    print('collision')
                    wrong_answer1 = answer[1]
                    start_time -= add_time # decrease time when box is clicked
                    # add move on to the next question code
                    time_warp.play()
                    popped_obj = copied_question_list.pop()
                    q_text = popped_obj.question_text
                    answer = popped_obj.answers
                    counter += 1

                if box_rect2.collidepoint(event.pos):
                    wrong_answer2 = answer[2]
                    print('collision') #clicking on this box neither increase or decrease time
                    # add move on to the next question code
                    popped_obj = copied_question_list.pop()
                    q_text = popped_obj.question_text
                    answer = popped_obj.answers
                    counter += 1

                if box_rect3.collidepoint(event.pos):
                    wrong_answer3 = answer[3]
                    print('collision')
                    start_time = 0 # kills the time when box is clicked
                    # add move on to the next question code
                    popped_obj = copied_question_list.pop()
                    q_text = popped_obj.question_text
                    answer = popped_obj.answers
                    counter += 1
                    destroyer_sound.play()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and box_intro_rect.collidepoint(event.pos):
                # resetgame()
                game_active = True
                start_time += int(pygame.time.get_ticks() / 1000)
             
    if game_active and copied_question_list is not None:
        space.play()
        intro_sound.stop()
        question_box = question_font.render(f'{counter}: {q_text}', False, (111, 196, 170))
        question_box_rect = question_box.get_rect(center = (750, 100))

        screen.blit(question_box, question_box_rect)

        # box_gravity += 0.005 #this moves the box faster
        # box_rect.x += box_gravity

        ################################################################################
        ################################################################################
        ################################################################################

        screen.blit(box_surface, box_rect) #blit grabs the rectangle drawn around the itemm surface from (midbottom) point from when we created the rect, and depends the point being grabbed, it positions the surface on x,y axis position: 400px to the left by 200px from the top
        screen.blit(box_surface1, box_rect1)
        screen.blit(box_surface2, box_rect2)
        screen.blit(box_surface3, box_rect3)

        """
        When we're on Level 1,
            we blit the box with answers on screen.
        When we're on Level 2->,
            we blit over the original box with a new blank box and new answer.
        ...
        """

        if counter == 1:
            #boxes with answers
            answer_surface, answer_rect = render_wrapped_text(f'{answer[0]}', test_font, (111, 196, 170), box_rect.width, box_rect.height)
            # answer_surface1 = test_font.render(f'{answer[1]}', False, (111, 196, 170))
            answer_surface1, answer_rect1 = render_wrapped_text(f'{answer[1]}', test_font, (111, 196, 170), box_rect1.width, box_rect1.height)
            answer_surface2, answer_rect2 = render_wrapped_text(f'{answer[2]}', test_font, (111, 196, 170), box_rect2.width, box_rect2.height)
            answer_surface3, answer_rect3 = render_wrapped_text(f'{answer[3]}', test_font, (111, 196, 170), box_rect3.width, box_rect3.height)

            # SUCCESSFUL RENDER AND CONNECTION OF RED BOX TO RED TEXT
            box_surface.blit(answer_surface, answer_rect)

            # ATTEMPT TO FIX RENDER/CONNNECTION OF BLUE-TO-BLUE BOX-TO-RECT
            box_surface1.blit(answer_surface1, answer_rect1)

            # SUCCESSFUL RENDER AND CONNECTION OF GREEN BOX TO GREEN TEXT
            box_surface2.blit(answer_surface2, answer_rect2)

            # SUCCESSFUL RENDER AND CONNECTION OF YELLOW BOX TO YELLOW TEXT
            box_surface3.blit(answer_surface3, answer_rect3)

        elif counter > 1:
            # Create new region for new red box content
            new_red_region = pygame.Surface((200, 200))
            new_red_region.fill("Red")
            new_red_rectangle = new_red_region.get_rect(midbottom = (750,300))
            # Extract new game objects for updated red box answers
            answer_surface, answer_rect = render_wrapped_text(f'{answer[0]}', test_font, (111, 196, 170), box_rect.width, box_rect.height)
            # Render updated red box answers to newly created red region
            new_red_region.blit(answer_surface, answer_rect)
            # Render new red region to screen
            screen.blit(new_red_region, box_rect)

            # Create new region for new blue box content
            new_blue_region = pygame.Surface((200, 200))
            new_blue_region.fill("Blue")
            new_blue_rectangle = new_blue_region.get_rect(midbottom = (750,300))
            # Extract new game objects for updated red box answers
            answer_surface1, answer_rect1 = render_wrapped_text(f'{answer[1]}', test_font, (111, 196, 170), box_rect1.width, box_rect1.height)
            # Render updated red box answers to newly created red region
            new_blue_region.blit(answer_surface1, answer_rect1)
            # Render new red region to screen
            screen.blit(new_blue_region, box_rect1)

            # Create new region for new red box content
            new_green_region = pygame.Surface((200, 200))
            new_green_region.fill("Green")
            new_green_rectangle = new_green_region.get_rect(midbottom = (750,300))
            # Extract new game objects for updated red box answers
            answer_surface2, answer_rect2 = render_wrapped_text(f'{answer[2]}', test_font, (111, 196, 170), box_rect2.width, box_rect2.height)
            # Render updated red box answers to newly created red region
            new_green_region.blit(answer_surface2, answer_rect2)
            # Render new red region to screen
            screen.blit(new_green_region, box_rect2)

            # Create new region for new red box content
            new_yellow_region = pygame.Surface((200, 200))
            new_yellow_region.fill("Yellow")
            new_yellow_rectangle = new_yellow_region.get_rect(midbottom = (750,300))
            # Extract new game objects for updated red box answers
            answer_surface3, answer_rect3 = render_wrapped_text(f'{answer[3]}', test_font, (111, 196, 170), box_rect3.width, box_rect3.height)
            # Render updated red box answers to newly created red region
            new_yellow_region.blit(answer_surface3, answer_rect3)
            # Render new red region to screen
            screen.blit(new_yellow_region, box_rect3)


        ################################################################################
        ################################################################################
        ################################################################################

        # UNSUCCESSFUL RENDER AND CONNECTION OF BLUE BOX TO BLUE TEXT
        # screen.blit(answer_surface1, (box_rect1.x, box_rect1.y))
        # box_surface1.blit(answer_surface1, answer_rect1)
        # screen.blit(answer_surface1, box_rect1)
        
        # box_rect.x += 10 #moves the box on x axis
        # Attempting to randomly move box in both X and Y
        
        box_rect.x += randint(-20, 20)
        box_rect.y += randint(-20, 20)
        if box_rect.right >= 950: box_rect.left = 0 #places box on other side of screen after the box goes beyond the screen. remember screen is 800px on x and y axis. so it waits till it disappears after 1000px then spawns it on the opposite side at 0px 
        elif box_rect.left <= 0: box_rect.right = 950
        elif box_rect.bottom >= 950: box_rect.top = 0
        elif box_rect.top <= 0: box_rect.bottom = 950

        # NOTE: This 
        # screen.blit(blue_box_clickable_region, blue_box_rectangle_visual)
        # blue_box_clickable_region.blit(blue_answer_clickable_region, blue_answer_rectangle_visual)
        
        # box_rect1.x -= 5
        box_rect1.x += randint(-20, 20)
        box_rect1.y += randint(-20, 20)
        if box_rect1.left <= 0: box_rect1.right = 1500
        elif box_rect1.left <= 0: box_rect1.right = 1500
        elif box_rect1.bottom >= 1500: box_rect1.top = 0
        elif box_rect1.top <= 0: box_rect1.bottom = 1500
        
        # box_rect2.x += 10
        box_rect2.x += randint(-20, 20)
        box_rect2.y += randint(-20, 20)
        if box_rect2.right >= 1500: box_rect2.left = 0
        elif box_rect2.left <= 0: box_rect2.right = 1500
        elif box_rect2.bottom >= 1500: box_rect2.top = 0
        elif box_rect2.top <= 0: box_rect2.bottom = 1500

        # screen.blit(answer_surface3, (box_rect3.x, box_rect3.y))
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
        if clock.tick(10) and shake_timer >= 10:
            shake_timer = time.time()
            # Shake the box by adjusting its position randomly
            box_intro_rect.x += randint(-20, 20)
            box_intro_rect.y += randint(-20, 20)
        # space_hole = pygame.image.load('lib/backdrop/blackhole2.png').convert()
        # space_hole = pygame.transform.scale(box_intro, (0,0))

        screen.blit(box_intro, box_intro_rect)
        # screen.blit(space_hole, (box_intro_rect.x, box_intro_rect.y))
        screen.blit(title_surface, title_rect)
        screen.blit(title_message, title_message_rect)
        intro_sound.play()
        space.stop()

    pygame.display.update()
    clock.tick(60)