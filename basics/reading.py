file = open("scores.txt", "r")

participants = {}

for line in file:
    entry = line.strip().split(",") # remove the following \n and create a list from a dictionary record
    participant = entry[0]
    score = entry[1]
    participants[participant] = score
    print(participant + ": " + score)

file.close()

print(participants)
