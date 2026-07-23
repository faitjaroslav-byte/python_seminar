import random
import string

adjectives = ["sleepy", "slow", "red", "green", "brave", "proud"]
nouns = ["apple", "dinosaur", "panda", "rocket", "dragon"]

print("Password Picker")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("Your new password is:", password)

    response = input("Would you like another password? Type y or n: ")
    if response == "n":
        break
