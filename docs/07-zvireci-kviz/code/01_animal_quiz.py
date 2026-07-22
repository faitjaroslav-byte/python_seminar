score = 0

print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole? ")
if guess1 == "polar bear":
    print("Correct answer")
    score = score + 1

guess2 = input("Which is the fastest land animal? ")
if guess2 == "cheetah":
    print("Correct answer")
    score = score + 1

guess3 = input("Which is the largest animal? ")
if guess3 == "blue whale":
    print("Correct answer")
    score = score + 1

print("Your score is " + str(score))
