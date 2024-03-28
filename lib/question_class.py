class Question:

    all_questions = []

    def __init__(self, category, question_text, answers, correct_indx):
        self.category = category
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


q1 = Question('Python', 'What is the output of the following Python code? print(2 + 2)', 
              answers=[4, 5, 3, 2], correct_indx=0)

q2 = Question('Python', 'What does the len() function in Python do?', 
              answers=['Computes the square root of a number',
                       'Returns the length of a list or string', 
                       'Performs a bitwise AND operation', 
                       'Raises a number to a power'], correct_indx=1)
        
q3 = Question('Python', 'What is the correct way to comment out a single line in Python?', 
              answers=['// Comment', '<!-- Comment -->', '/* Comment */', '# Comment'], correct_indx=3)

q4 = Question('Python', 'Which of the following data types is mutable in Python?', 
              answers=['Integer', 'Tuple', 'List', 'String'], correct_indx=2)
                
q5 = Question('Python', 'What is the result of the expression 3 * \'abc\' in Python?', 
              answers=['\'abc abc abc\'', '\'abcabc\'', '\'abcabcabc\'', '\'abc\''], correct_indx=2)

q6 = Question('Python', 'Which of the following statements is used to exit from a loop in Python?', 
              answers=['pass', 'break', 'None', 'continue'], correct_indx=1)

q7 = Question('Python', 'What is the output of the following code? ("Python"[::-1])', 
              answers=['\'nohtyP\'', '\'Python\'', '\'Pyth\'', '\'ytho\''], correct_indx=0)

q8 = Question('Python', 'What method in Python is used to add an element to the end of a list?', 
              answers=['add()', 'insert()', 'extend()', 'append()'], correct_indx=3)

q9 = Question('Python', 'What does the __init__ method in Python represent?', 
              answers=['Destructor method', 'Class method', 'Constructor method', 'Inheritance method'], correct_indx=2)

q10 = Question('Python', 'How do you iterate over both indices and elements in an iterable?', 
              answers=['enumerate(iterable)', 'enumerate(iterable, start=1)', 'range(iterable)', 'range(iterable, start=1)'], correct_indx=0)

class Category:
    def __init__(self, category):
        self.category = category
        pass

def question_call():
    for question in Question.all_questions:
        question.ask_user()

def intro():
    input('Would you like to play: \nyes or no')

# question_call()
        