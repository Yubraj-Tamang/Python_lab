# Basic Quiz App Requirement 
- Description: A program that asks the user multiple-choice questions, calculates their score, and provides feedback.

- **Features:**
    - Store questions, options, and correct answers using dictionaries.
    - Accept user input for answers.
    - Display the user's final score.

# Documentation: Basic Quiz App

## Overview
The Basic Quiz App is a Python program designed to test users' knowledge by answering multiple-choice questions. It tracks the user's score and provides feedback at the end of the quiz.

## Features
1. **Multiple-Choice Questions**: Each question includes four answer options.
2. **User Input**: Users select their answers by entering the corresponding option.
3. **Answer Validation**: The app checks if the selected answer is correct or incorrect.
4. **Score Tracking**: Keeps track of correct answers and calculates the total score.
5. **Final Feedback**: Displays the user's final score at the end of the quiz.

## Functionalities

### 1. Question Display
- **Input**: Presents a question and its multiple-choice options to the user.
- **Output**: Prompts the user to select an answer.

### 2. Answer Validation
- Compares the user's selected answer with the correct one.
- Provides immediate feedback (Correct/Wrong).

### 3. Score Tracking
- Updates the score for each correct answer.

### 4. Final Feedback
- Displays the total score out of the total number of questions.

## Sample Code
```python
# Quiz App
questions = {
    "What is the capital of Nepal?": ["a) Kathmandu", "b) Biratnagar", "c) Pokhara", "d) Lumbini"],
    "What is 5 + 3?": ["a) 5", "b) 8", "c) 10", "d) 15"],
    "Which programming language is known as Python?": ["a) Java", "b) C++", "c) Python", "d) Ruby"],
}

answers = {
    "What is the capital of Nepal?": "a",
    "What is 5 + 3?": "b",
    "Which programming language is known as Python?": "c",
}

def quiz():
    print("Welcome to the Quiz App!")
    score = 0
    for question, options in questions.items():
        print("\n" + question)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ").lower()
        if answer == answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"\nYour final score is: {score}/{len(questions)}")

quiz()
```

## How to Run
1. Run the file or execute in the python interpreter (`quiz_app.py`).
2. Run the file in a Python interpreter.
3. Answer the questions displayed during the quiz.

## Example Interaction
```
Welcome to the Quiz App!

What is the capital of Nepal?
a) Kathmandu
b) Biratnagar
c) Pokhara
d) Lumbini
Enter your answer (a/b/c/d): a
Correct!

What is 5 + 3?
a) 5
b) 8
c) 10
d) 15
Enter your answer (a/b/c/d): b
Correct!

Which programming language is known as Python?
a) Java
b) C++
c) Python
d) Ruby
Enter your answer (a/b/c/d): c
Correct!

Your final score is: 3/3
```

## Key Topics Covered
- **Dictionaries**: Store questions and answers.
- **Loops**: Iterate through questions.
- **Conditionals**: Validate answers.
- **Input/Output**: Interact with the user.

## Customization Ideas
- Add more questions to the `questions` and `answers` dictionaries.
- Implement difficulty levels (easy, medium, hard).
- Introduce a timer for answering questions.

