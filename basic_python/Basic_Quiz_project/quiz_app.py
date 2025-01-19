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
