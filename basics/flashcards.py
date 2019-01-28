import sys
import random

if len(sys.argv) < 2:
    print("supply a flashcard file")
    exit(1)

flashcard_filename = sys.argv[1]
file = open(flashcard_filename, "r")

question_dict = {}

for line in file:
    entry = line.strip().split(",")
    question = entry[0]
    answer = entry[1]
    question_dict[question] = answer

file.close()

print("wecome to flashcard quizzer")
print("at any time type 'quit' to quit")
print("")

questions = list(question_dict.keys())

while True: 
    question = random.choice(questions)
    answer = question_dict[question]

    print("question: " + question)
    user_input = input("your guess")
    if user_input == "quit":
        print("thanks for playing")
        break
    elif user_input == answer:
        print("correct!")
    else:
        print("sorry, the answer was: " + answer)
