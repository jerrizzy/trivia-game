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

    def __init__(self):
        pass

        