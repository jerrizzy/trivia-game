import pygame
from sys import exit

def display_score():
    current_time = start_time - int(pygame.time.get_ticks() / 1000)
    current_time = max(0, current_time)
    score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    return current_time

def display_answers():
    global current_question_index

    question = python_questions_list[current_question_index]
    options = question["options"]

    # Red Box
    correct_answer_surface = small_font.render(question["answer"], True, (0, 0, 0))
    correct_answer_rect = correct_answer_surface.get_rect(center=(box_rect.x + box_rect.width // 2, box_rect.y + box_rect.height // 2))
    screen.blit(correct_answer_surface, correct_answer_rect)

    # Blue Box
    blue_answer_surface = small_font.render(options[0], True, (0, 0, 0))
    blue_answer_rect = blue_answer_surface.get_rect(center=(box_rect1.x + box_rect1.width // 2, box_rect1.y + box_rect1.height // 2))
    screen.blit(blue_answer_surface, blue_answer_rect)

    # Green Box
    green_answer_surface = small_font.render(options[1], True, (0, 0, 0))
    green_answer_rect = green_answer_surface.get_rect(center=(box_rect2.x + box_rect2.width // 2, box_rect2.y + box_rect2.height // 2))
    screen.blit(green_answer_surface, green_answer_rect)

    # Yellow Box
    yellow_answer_surface = small_font.render(options[2], True, (0, 0, 0))
    yellow_answer_rect = yellow_answer_surface.get_rect(center=(box_rect3.x + box_rect3.width // 2, box_rect3.y + box_rect3.height // 2))
    screen.blit(yellow_answer_surface, yellow_answer_rect)

def display_questions():
    if current_question_index != -1:
        question = python_questions_list[current_question_index]["question"]
        question_surface = test_font.render(question, True, (0, 0, 0))
        question_rect = question_surface.get_rect(midtop=(400, 100))
        screen.blit(question_surface, question_rect)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Blade')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

box_surface = pygame.Surface((200, 100))
box_surface.fill('Red')
box_rect = box_surface.get_rect(midbottom=(400, 250))

box_surface1 = pygame.Surface((200, 100))
box_surface1.fill('Blue')
box_rect1 = box_surface1.get_rect(midbottom=(400, 370))

box_surface2 = pygame.Surface((200, 100))
box_surface2.fill('Green')
box_rect2 = box_surface2.get_rect(midbottom=(400, 490))

box_surface3 = pygame.Surface((200, 100))
box_surface3.fill('Yellow')
box_rect3 = box_surface3.get_rect(midbottom=(400, 610))

start_time = 30
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
    # Add more questions as needed
]
current_question_index = -1

game_active = True

while True:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# this event handler is what controls the event clicks of the boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                current_question_index = (current_question_index + 1) % len(python_questions_list)
                start_time += 5

            if box_rect1.collidepoint(event.pos):
                current_question_index = (current_question_index + 1) % len(python_questions_list)
                start_time -= 5

            if box_rect2.collidepoint(event.pos):
                current_question_index = (current_question_index + 1) % len(python_questions_list)

            if box_rect3.collidepoint(event.pos):
                start_time = 0

    if game_active:
        screen.blit(box_surface, box_rect)
        box_rect.x += 5
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
        display_questions()
        display_answers()

        if display_score() == 0:
            game_active = False
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60)