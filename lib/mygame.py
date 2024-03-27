import pygame
from sys import exit
from random import choice

def display_score():
    current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time)  # Ensure current_time doesn't go below 0
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    return current_time

def display_python_question():
    global current_question_index
    question = python_questions_list[current_question_index]
    question_surface = test_font.render(question["question"], True, (0, 0, 0))
    question_rect = question_surface.get_rect(topleft=(10, 100))
    screen.blit(question_surface, question_rect)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Blade')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 36)

box_surface = pygame.Surface((200, 100))  # Rectangle shape
box_surface.fill('Red')
box_rect = box_surface.get_rect(midbottom=(400, 250))

box_surface1 = pygame.Surface((200, 100))  # Rectangle shape
box_surface1.fill('Blue')
box_rect1 = box_surface1.get_rect(midbottom=(400, 370))

box_surface2 = pygame.Surface((200, 100))  # Rectangle shape
box_surface2.fill('Green')
box_rect2 = box_surface2.get_rect(midbottom=(400, 490))

box_surface3 = pygame.Surface((200, 100))  # Rectangle shape
box_surface3.fill('Yellow')
box_rect3 = box_surface3.get_rect(midbottom=(400, 610))

start_time = 30  # Set the initial time to 30 seconds
python_questions_list = [
    {
        "question": "What is Python?",
        "options": [
            "A. A type of snake",
            "B. A programming language",
            "C. A text editor",
            "D. A web browser"
        ],
        "answer": "B. A programming language"
    },
    {
        "question": "What does 'print()' do in Python?",
        "options": [
            "A. Displays output on the screen",
            "B. Reads input from the user",
            "C. Executes a loop",
            "D. Defines a function"
        ],
        "answer": "A. Displays output on the screen"
    },
    {
        "question": "What is JavaScript?",
        "options": [
            "A. A type of coffee",
            "B. A programming language",
            "C. A database system",
            "D. An operating system"
        ],
        "answer": "B. A programming language"
    },
    {
        "question": "How do you define a variable in JavaScript?",
        "options": [
            "A. var x = 5;",
            "B. int x = 5;",
            "C. variable x = 5;",
            "D. x = 5;"
        ],
        "answer": "A. var x = 5;"
    },
    {
        "question": "What is React?",
        "options": [
            "A. A programming language",
            "B. A JavaScript library for building user interfaces",
            "C. A server-side framework",
            "D. An operating system"
        ],
        "answer": "B. A JavaScript library for building user interfaces"
    },
    {
        "question": "What does 'JSX' stand for in React?",
        "options": [
            "A. JavaScript XML",
            "B. JavaScript Extensible",
            "C. JavaScript Xtra",
            "D. Java Standard Extension"
        ],
        "answer": "A. JavaScript XML"
    }
]
current_question_index = -1  # Index of the current question being displayed

game_active = True

while True:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                current_question_index = (current_question_index + 1) % len(python_questions_list)
                start_time += 5  # Add 5 seconds to the timer

            if box_rect1.collidepoint(event.pos):
                print('collision')
                start_time -= 5

            if box_rect2.collidepoint(event.pos):
                print('collision')  # Clicking on this box neither increases nor decreases time

            if box_rect3.collidepoint(event.pos):
                print('collision')
                start_time = 0

    if game_active:
        screen.blit(box_surface, box_rect)
        box_rect.x += 5  # Adjusted movement speed
        if box_rect.right >= 800:
            box_rect.left = 0

        screen.blit(box_surface1, box_rect1)
        box_rect1.x -= 5
        if box_rect1.left <= 0:
            box_rect1.right = 800

        screen.blit(box_surface2, box_rect2)
        box_rect2.x += 5
        if box_rect2.right >= 800:
            box_rect2.left = 0

        screen.blit(box_surface3, box_rect3)
        box_rect3.x -= 5
        if box_rect3.left <= 0:
            box_rect3.right = 800

        display_score()
        if current_question_index != -1:
            display_python_question()

        if display_score() == 0:
            game_active = False
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60)

















