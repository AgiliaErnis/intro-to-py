file = open("scores.txt", "w")

while True:
    participant = input("Participant name: ")

    if participant == "quit":
        print("quitting...")
        break

    score = input("Score for "+participant+" is: ")
    file.write(participant+","+score+"\n")

file.close()
