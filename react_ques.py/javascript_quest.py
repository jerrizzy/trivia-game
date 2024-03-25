LEVELS = {
    'add': 1,
    'subtract': 2,
    'none': 3
}
javascript_questions = [
    {
        'category': 'JavaScript',
        'questions': [
            {
                'text': 'What is the result of the following JavaScript expression?\n5 + 3',
                'answers': [
                    {'text': '8', 'level': LEVELS['add']},
                    {'text': '2', 'level': LEVELS['subtract']},
                    {'text': '15', 'level': LEVELS['none']},
                    {'text': '53', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you declare a variable in JavaScript?',
                'answers': [
                    {'text': 'Using the "var", "let", or "const" keyword', 'level': LEVELS['add']},
                    {'text': 'Using the "variable" keyword', 'level': LEVELS['subtract']},
                    {'text': 'Using the "int" keyword', 'level': LEVELS['none']},
                    {'text': 'Using the "string" keyword', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What does the "console.log()" function do in JavaScript?',
                'answers': [
                    {'text': 'Prints a message or object to the browser console', 'level': LEVELS['add']},
                    {'text': 'Creates a pop-up dialog box', 'level': LEVELS['subtract']},
                    {'text': 'Sends an HTTP request', 'level': LEVELS['none']},
                    {'text': 'Renders HTML content', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the result of the following JavaScript expression?\n"5" + "3"',
                'answers': [
                    {'text': '"53"', 'level': LEVELS['add']},
                    {'text': '"8"', 'level': LEVELS['subtract']},
                    {'text': '"15"', 'level': LEVELS['none']},
                    {'text': '8', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you define a function in JavaScript?',
                'answers': [
                    {'text': 'Using the "function" keyword', 'level': LEVELS['add']},
                    {'text': 'Using the "def" keyword', 'level': LEVELS['subtract']},
                    {'text': 'Using the "method" keyword', 'level': LEVELS['none']},
                    {'text': 'Using the "func" keyword', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the result of the following JavaScript expression?\n5 === "5"',
                'answers': [
                    {'text': 'false', 'level': LEVELS['add']},
                    {'text': 'true', 'level': LEVELS['subtract']},
                    {'text': 'undefined', 'level': LEVELS['none']},
                    {'text': 'null', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What does the "typeof" operator do in JavaScript?',
                'answers': [
                    {'text': 'Returns the data type of a variable or expression', 'level': LEVELS['add']},
                    {'text': 'Converts a value to a string', 'level': LEVELS['subtract']},
                    {'text': 'Performs mathematical operations', 'level': LEVELS['none']},
                    {'text': 'Creates a new object', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the result of the following JavaScript expression?\n[1, 2, 3].length',
                'answers': [
                    {'text': '3', 'level': LEVELS['add']},
                    {'text': '6', 'level': LEVELS['subtract']},
                    {'text': '0', 'level': LEVELS['none']},
                    {'text': 'undefined', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the purpose of the "return" statement in a JavaScript function?',
                'answers': [
                    {'text': 'Specifies the value to be returned by the function', 'level': LEVELS['add']},
                    {'text': 'Prints a message to the console', 'level': LEVELS['subtract']},
                    {'text': 'Ends the execution of the function', 'level': LEVELS['none']},
                    {'text': 'Defines a variable', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you add a comment in JavaScript?',
                'answers': [
                    {'text': '// This is a comment', 'level': LEVELS['add']},
                    {'text': '# This is a comment', 'level': LEVELS['subtract']},
                    {'text': '<!-- This is a comment -->', 'level': LEVELS['none']},
                    {'text': '/* This is a comment */', 'level': LEVELS['none']}
                ]
            },
        ]
    },
]
