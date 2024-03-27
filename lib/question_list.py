 # Define levels of answers
# LEVELS = {
#     'add': 1,
#     'subtract': 2,
#     'none': 3
# }

# # List of dictionaries to hold questions and answers for each category
# all_questions = [
#     {
#         'category': 'Python',
#         'questions': [
#             {
#                 'text': 'What is the output of the following Python code?\nprint(2 + 2)',
#                 'answers': [
#                     {'text': '4', 'level': LEVELS['add']},
#                     {'text': '5', 'level': LEVELS['subtract']},
#                     {'text': '3', 'level': LEVELS['none']},
#                     {'text': '2', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What does the len() function in Python do?',
#                 'answers': [
#                     {'text': 'Returns the length of a list or string', 'level': LEVELS['add']},
#                     {'text': 'Computes the square root of a number', 'level': LEVELS['subtract']},
#                     {'text': 'Performs a bitwise AND operation', 'level': LEVELS['none']},
#                     {'text': 'Raises a number to a power', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What is the correct way to comment out a single line in Python?',
#                 'answers': [
#                     {'text': '# Comment', 'level': LEVELS['add']},
#                     {'text': '// Comment', 'level': LEVELS['subtract']},
#                     {'text': '/* Comment */', 'level': LEVELS['none']},
#                     {'text': '<!-- Comment -->', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'Which of the following data types is mutable in Python?',
#                 'answers': [
#                     {'text': 'List', 'level': LEVELS['add']},
#                     {'text': 'String', 'level': LEVELS['none']},
#                     {'text': 'Integer', 'level': LEVELS['subtract']},
#                     {'text': 'Tuple', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What is the result of the expression 3 * \'abc\' in Python?',
#                 'answers': [
#                     {'text': '\'abcabcabc\'', 'level': LEVELS['add']},
#                     {'text': '\'abcabc\'', 'level': LEVELS['subtract']},
#                     {'text': '\'abc\'', 'level': LEVELS['none']},
#                     {'text': '\'abc abc abc\'', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'Which of the following statements is used to exit from a loop in Python?',
#                 'answers': [
#                     {'text': 'break', 'level': LEVELS['add']},
#                     {'text': 'stop', 'level': LEVELS['subtract']},
#                     {'text': 'halt', 'level': LEVELS['none']},
#                     {'text': 'end', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What is the output of the following code?\nprint("Python"[::-1])',
#                 'answers': [
#                     {'text': '\'nohtyP\'', 'level': LEVELS['add']},
#                     {'text': '\'Python\'', 'level': LEVELS['subtract']},
#                     {'text': '\'Pyth\'', 'level': LEVELS['none']},
#                     {'text': '\'ytho\'', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What method in Python is used to add an element to the end of a list?',
#                 'answers': [
#                     {'text': 'append()', 'level': LEVELS['add']},
#                     {'text': 'add()', 'level': LEVELS['subtract']},
#                     {'text': 'insert()', 'level': LEVELS['none']},
#                     {'text': 'extend()', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'What does the __init__ method in Python represent?',
#                 'answers': [
#                     {'text': 'Constructor method', 'level': LEVELS['add']},
#                     {'text': 'Destructor method', 'level': LEVELS['subtract']},
#                     {'text': 'Class method', 'level': LEVELS['none']},
#                     {'text': 'Inheritance method', 'level': LEVELS['none']}
#                 ]
#             },
#             {
#                 'text': 'Which of the following statements is used to declare a function in Python?',
#                 'answers': [
#                     {'text': 'def function():', 'level': LEVELS['add']},
#                     {'text': 'function() { }', 'level': LEVELS['subtract']},
#                     {'text': 'func def() { }', 'level': LEVELS['none']},
#                     {'text': 'declare function():', 'level': LEVELS['none']}
#                 ]
#             }
#         ]
#     }
#     # Add more
# ]




# import pygame
# from sys import exit
# from random import randint



# def display_score():
#     current_time = start_time - int(pygame.time.get_ticks() / 1000)
#     current_time = max(0, current_time) # Ensure current_time doesn't go below 0
#     score_surface = test_font.render(f'Time Alive: {current_time}', False, (64, 64, 64))
#     score_rect = score_surface.get_rect(center = (400, 50))
#     pygame.draw.rect(screen, '#c0e8ec', score_rect)
#     pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
#     screen.blit(score_surface, score_rect)
#     return current_time

# start_time = 30 # Set the initial time to 60 seconds

# python_questionsjs = [
#     {
#         "question": "What is JavaScript commonly used for in web development?",
#         "options": [
#             "A. Styling web pages",
#             "B. Server-side scripting",
#             "C. Adding interactivity to web pages",
#             "D. Querying databases"
#         ],
#         "answer": "C. Adding interactivity to web pages"
#     },
#     {
#         "question": "What is React?",
#         "options": [
#             "A. A programming language",
#             "B. A JavaScript library for building user interfaces",
#             "C. A server-side framework",
#             "D. An operating system"
#         ],
#         "answer": "B. A JavaScript library for building user interfaces"
#     },
#     {
#         "question": "What is Python commonly used for?",
#         "options": [
#             "A. Frontend web development",
#             "B. Data analysis and scientific computing",
#             "C. Database management",
#             "D. Network security"
#         ],
#         "answer": "B. Data analysis and scientific computing"
#     },
#     # Add more questions as needed
# ]

# def python_questions():
#     question = random.choice(python_questionsjs)
#     question_surface = test_font.render(question, True, (0, 0, 0))
#     question_rect = question_surface.get_rect(topright=(780, 100))
#     screen.blit(question_surface, question_rect)
# # python_questions()

# pygame.init() # this function starts pygame. like starting a car with a key
# screen = pygame.display.set_mode((800, 800)) # this is our (display surface). Point of origin 
# #The window our player sees. first number is width, sencond one 
# #is height of the window. set_mode function takes at least 1 argument, in this case a tuple

# pygame.display.set_caption('Blade')# it names the game on the window
# clock = pygame.time.Clock() #Clock object keeps track of time and control frame rate. Here it does nothing, it's being called in the while loop
# test_font = pygame.font.Font('lib/font/Pixeltype.ttf', 50) #this works with our variable text_surface. It determines the kind of font, and size

# # boxes
# box_surface = pygame.Surface((100, 100)) # this creates item. tuple is the size of item = 100px by 100px
# box_surface.fill('Red') #gives item color
# box_rect = box_surface.get_rect(midbottom = (400,250)) #get_rect is rectangle to contain the item so that it can be controlled. x,y axis position: 400px to the left by 200px from the top.

# box_surface1 = pygame.Surface((100, 100)) 
# box_surface1.fill('Blue')
# box_rect1 = box_surface1.get_rect(midbottom = (400,370))

# box_surface2 = pygame.Surface((100, 100)) 
# box_surface2.fill('Green')
# box_rect2 = box_surface2.get_rect(midbottom = (400,490))

# box_surface3 = pygame.Surface((100, 100)) 
# box_surface3.fill('Yellow')
# box_rect3 = box_surface3.get_rect(midbottom = (400,610))

# box_gravity = 0

# add_time = 5

# game_acive = True


# while True:
#     screen.fill(('white'))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()# this quits the game
#             exit()

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if box_rect.collidepoint(event.pos):
#                 print('collision')
#                 start_time += add_time # adds time when box is clicked
#                 # add move on to the next question code

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if box_rect1.collidepoint(event.pos):
#                 print('collision')
#                 start_time -= add_time # decrease time when box is clicked
#                 # add move on to the next question code

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if box_rect2.collidepoint(event.pos):
#                 print('collision') #clicking on this box neither increase or decrease time
#                 # add move on to the next question code

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if box_rect3.collidepoint(event.pos):
#                 print('collision')
#                 start_time = 0 # kills the time when box is clicked
#                 # add move on to the next question code
                
#     if game_acive:       
#         # box_gravity += 0.005 #this moves the box faster
#         # box_rect.x += box_gravity
#         screen.blit(box_surface, box_rect) #blit grabs the rectangle drawn around the itemm surface from (midbottom) point from when we created the rect, and depends the point being grabbed, it positions the surface on x,y axis position: 400px to the left by 200px from the top
#         box_rect.x += 10
#         if box_rect.right >= 1000: box_rect.left = 0

#         screen.blit(box_surface1, box_rect1) 
#         box_rect1.x -= 5
#         if box_rect1.left <= 0: box_rect1.right = 1000

#         screen.blit(box_surface2, box_rect2) 
#         box_rect2.x += 10
#         if box_rect2.right >= 1000: box_rect2.left = 0

#         screen.blit(box_surface3, box_rect3) 
#         box_rect3.x -= 5
#         if box_rect3.left <= 0: box_rect3.right = 1000
        

#         # mouse_pos = pygame.mouse.get_pos()
#         # if box_rect.collidepoint(mouse_pos):
#         #     print('collision')

#         display_score()
#         if display_score() == 0:
#             game_acive = False
#     else:
#         screen.fill('Red')


#     pygame.display.update()
#     clock.tick(60)
#     python_questions()