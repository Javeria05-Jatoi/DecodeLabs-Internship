import time

score = 0
total_questions = 5

questions = [
    {
        "question": "Q1: What is the capital of France?",
        "answer": "paris",
        "hint": "Paris"
    },
    {
        "question": "Q2: What is the largest planet in our solar system?",
        "answer": "jupiter",
        "hint": "Jupiter"
    },
    {
        "question": "Q3: How many sides does a hexagon have?",
        "answer": "6",
        "hint": "6 or six"
    },
    {
        "question": "Q4: What is the chemical symbol for water?",
        "answer": "h2o",
        "hint": "H2O"
    },
    {
        "question": "Q5: Who invented the telephone?",
        "answer": "alexander graham bell",
        "hint": "Alexander Graham Bell"
    }
]

while True:
    print("\n--- General Knowledge Quiz ---")
    print("Answer all 5 questions carefully!")
    print("--------------------------------------")

    score = 0
    start_time = time.time()

    for i, q in enumerate(questions, 1):
        answer = input(f"\n{q['question']} ").strip().lower()
        if answer == q["answer"] or answer == q["answer"].split()[0]:
            print("Correct! ✓")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['hint']}. ✗")

    end_time = time.time()
    time_taken = round(end_time - start_time)

    percentage = (score / total_questions) * 100

    print("\n--------------------------------------")
    print(f"Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    print(f"Percentage: {percentage}%")
    print(f"Time taken: {time_taken} seconds")

    if percentage == 100:
        print("Excellent! Perfect score! 🏆")
    elif percentage >= 80:
        print("Great job! Almost perfect! 😊")
    elif percentage >= 60:
        print("Good try! Keep practicing! 💪")
    elif percentage >= 40:
        print("Need more practice! 📚")
    else:
        print("Better luck next time! Keep learning! 📖")

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThanks for playing! Goodbye! 👋")
        break