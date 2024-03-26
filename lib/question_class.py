class Question:

    # Define levels of answers
    LEVELS = {
        'add': 1,
        'subtract': 2,
        'none': 3
    }

    # List of dictionaries to hold questions and answers for each category
    all_questions = [
        {
            'category': 'Python',
            'questions': [
                {
                    'text': 'What is the output of the following Python code?\nprint(2 + 2)',
                    'answers': [
                        {'text': '4', 'level': LEVELS['add']},
                        {'text': '5', 'level': LEVELS['subtract']},
                        {'text': '3', 'level': LEVELS['none']},
                        {'text': '2', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What does the len() function in Python do?',
                    'answers': [
                        {'text': 'Returns the length of a list or string', 'level': LEVELS['add']},
                        {'text': 'Computes the square root of a number', 'level': LEVELS['subtract']},
                        {'text': 'Performs a bitwise AND operation', 'level': LEVELS['none']},
                        {'text': 'Raises a number to a power', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What is the correct way to comment out a single line in Python?',
                    'answers': [
                        {'text': '# Comment', 'level': LEVELS['add']},
                        {'text': '// Comment', 'level': LEVELS['subtract']},
                        {'text': '/* Comment */', 'level': LEVELS['none']},
                        {'text': '<!-- Comment -->', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'Which of the following data types is mutable in Python?',
                    'answers': [
                        {'text': 'List', 'level': LEVELS['add']},
                        {'text': 'String', 'level': LEVELS['none']},
                        {'text': 'Integer', 'level': LEVELS['subtract']},
                        {'text': 'Tuple', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What is the result of the expression 3 * \'abc\' in Python?',
                    'answers': [
                        {'text': '\'abcabcabc\'', 'level': LEVELS['add']},
                        {'text': '\'abcabc\'', 'level': LEVELS['subtract']},
                        {'text': '\'abc\'', 'level': LEVELS['none']},
                        {'text': '\'abc abc abc\'', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'Which of the following statements is used to exit from a loop in Python?',
                    'answers': [
                        {'text': 'break', 'level': LEVELS['add']},
                        {'text': 'stop', 'level': LEVELS['subtract']},
                        {'text': 'halt', 'level': LEVELS['none']},
                        {'text': 'end', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What is the output of the following code?\nprint("Python"[::-1])',
                    'answers': [
                        {'text': '\'nohtyP\'', 'level': LEVELS['add']},
                        {'text': '\'Python\'', 'level': LEVELS['subtract']},
                        {'text': '\'Pyth\'', 'level': LEVELS['none']},
                        {'text': '\'ytho\'', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What method in Python is used to add an element to the end of a list?',
                    'answers': [
                        {'text': 'append()', 'level': LEVELS['add']},
                        {'text': 'add()', 'level': LEVELS['subtract']},
                        {'text': 'insert()', 'level': LEVELS['none']},
                        {'text': 'extend()', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'What does the __init__ method in Python represent?',
                    'answers': [
                        {'text': 'Constructor method', 'level': LEVELS['add']},
                        {'text': 'Destructor method', 'level': LEVELS['subtract']},
                        {'text': 'Class method', 'level': LEVELS['none']},
                        {'text': 'Inheritance method', 'level': LEVELS['none']}
                    ]
                },
                {
                    'text': 'Which of the following statements is used to declare a function in Python?',
                    'answers': [
                        {'text': 'def function():', 'level': LEVELS['add']},
                        {'text': 'function() { }', 'level': LEVELS['subtract']},
                        {'text': 'func def() { }', 'level': LEVELS['none']},
                        {'text': 'declare function():', 'level': LEVELS['none']}
                    ]
                }
            ]
        }
        # Add more
]
    all_questions = []

    def __init__(self, question_text, answers, correct_indx):
        self.question_text = question_text
        self.answers = answers
        self.correct_indx = correct_indx
        Question.all_questions.append(self)

    def ask_user(self):
        print(self.question_text)
        for i, answer_text in enumerate(self.answers):
            print(f'{i}: {answer_text}')
        user_answer_indx = int(input('Enter your answer: '))
        if user_answer_indx == self.correct_indx:
            print('correct!')
        else:
            print('incorrect!')


q1 = Question('What is the output of the following Python code?\nprint(2 + 2)', 
              answers=[4, 5, 3, 2], correct_indx=0)

q2 = Question('What does the len() function in Python do?', 
              answers=['Computes the square root of a number',
                       'Returns the length of a list or string', 
                       'Performs a bitwise AND operation', 
                       'Raises a number to a power'], correct_indx=1)
        
q3 = Question('What is the correct way to comment out a single line in Python?', 
              answers=['// Comment', '<!-- Comment -->', '/* Comment */', '# Comment'], correct_indx=3)

q4 = Question('Which of the following data types is mutable in Python?', 
              answers=['Integer', 'Tuple', 'List', 'String'], correct_indx=2)
                
q5 = Question('What is the result of the expression 3 * \'abc\' in Python?', 
              answers=['\'abc abc abc\'', '\'abcabc\'', '\'abcabcabc\'', '\'abc\''], correct_indx=2)

q6 = Question('Which of the following statements is used to exit from a loop in Python?', 
              answers=['pass', 'break', 'None', 'continue'], correct_indx=1)

q7 = Question('What is the output of the following code?\nprint("Python"[::-1])', 
              answers=['\'nohtyP\'', '\'Python\'', '\'Pyth\'', '\'ytho\''], correct_indx=0)

q8 = Question('What method in Python is used to add an element to the end of a list?', 
              answers=['add()', 'insert()', 'extend()', 'append()'], correct_indx=3)

q9 = Question('What does the __init__ method in Python represent?', 
              answers=['Destructor method', 'Class method', 'Constructor method', 'Inheritance method'], correct_indx=2)

q10 = Question('Which of the following statements is used to declare a function in Python?', 
              answers=['def function():', 'function() { }', 'func def() { }', 'declare function():'], correct_indx=0)

class Category:
    def __init__(self, category):
        self.category = category
        pass

def question_call():
    for question in Question.all_questions:
        question.ask_user()

question_call()


        