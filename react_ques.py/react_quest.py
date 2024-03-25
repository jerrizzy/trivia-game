LEVELS = {
    'add': 1,
    'subtract': 2,
    'none': 3
}

react_questions = [
    {
        'category': 'React',
        'questions': [
            {
                'text': 'What does JSX stand for?',
                'answers': [
                    {'text': 'JavaScript XML', 'level': LEVELS['add']},
                    {'text': 'JavaScript Extension', 'level': LEVELS['subtract']},
                    {'text': 'JavaScript Syntax', 'level': LEVELS['none']},
                    {'text': 'Java Symbolic Expressions', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the entry point for a React application?',
                'answers': [
                    {'text': 'index.js', 'level': LEVELS['add']},
                    {'text': 'app.js', 'level': LEVELS['subtract']},
                    {'text': 'main.js', 'level': LEVELS['none']},
                    {'text': 'root.js', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What function is used to render a React component?',
                'answers': [
                    {'text': 'ReactDOM.render()', 'level': LEVELS['add']},
                    {'text': 'React.renderComponent()', 'level': LEVELS['subtract']},
                    {'text': 'React.render()', 'level': LEVELS['none']},
                    {'text': 'ReactDOM.mount()', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you define a stateful component in React?',
                'answers': [
                    {'text': 'Using a class component', 'level': LEVELS['add']},
                    {'text': 'Using a functional component', 'level': LEVELS['subtract']},
                    {'text': 'Using props', 'level': LEVELS['none']},
                    {'text': 'Using setState()', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the purpose of the useEffect hook in React?',
                'answers': [
                    {'text': 'To perform side effects in function components', 'level': LEVELS['add']},
                    {'text': 'To define state in class components', 'level': LEVELS['subtract']},
                    {'text': 'To handle routing in React applications', 'level': LEVELS['none']},
                    {'text': 'To create reusable component logic', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you update the state of a component in React?',
                'answers': [
                    {'text': 'Using the setState() method', 'level': LEVELS['add']},
                    {'text': 'Directly modifying the state object', 'level': LEVELS['subtract']},
                    {'text': 'Using props', 'level': LEVELS['none']},
                    {'text': 'Using the useEffect hook', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the purpose of props in React?',
                'answers': [
                    {'text': 'To pass data from parent to child components', 'level': LEVELS['add']},
                    {'text': 'To manage component state', 'level': LEVELS['subtract']},
                    {'text': 'To handle side effects in function components', 'level': LEVELS['none']},
                    {'text': 'To define component lifecycle methods', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'Which lifecycle method is invoked after a component has been updated?',
                'answers': [
                    {'text': 'componentDidUpdate()', 'level': LEVELS['add']},
                    {'text': 'componentWillUpdate()', 'level': LEVELS['subtract']},
                    {'text': 'componentWillReceiveProps()', 'level': LEVELS['none']},
                    {'text': 'componentDidMount()', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'What is the purpose of the key prop in React lists?',
                'answers': [
                    {'text': 'To uniquely identify elements and optimize rendering', 'level': LEVELS['add']},
                    {'text': 'To style list items', 'level': LEVELS['subtract']},
                    {'text': 'To filter list items', 'level': LEVELS['none']},
                    {'text': 'To define event handlers for list items', 'level': LEVELS['none']}
                ]
            },
            {
                'text': 'How do you conditionally render content in React?',
                'answers': [
                    {'text': 'Using conditional (ternary) operators or logical && operator', 'level': LEVELS['add']},
                    {'text': 'Using the useEffect hook', 'level': LEVELS['subtract']},
                    {'text': 'Using props', 'level': LEVELS['none']},
                    {'text': 'Using the setState() method', 'level': LEVELS['none']}
                ]
            },
        ]
    },
]
