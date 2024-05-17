import random

print("Welcome to the guessing game, you will enter a integer number and them we are going to create a random number that you must guess. ")

input_number = input("Enter a integer number up to 0: ")


if input_number.isdigit():
    input_number = int(input_number)

    if input_number <= 0:
        print("Please enter a number higher than 0")
        quit()
else:
    print("Enter a integer number next time.")
    quit()

random_number = random.randint(0, input_number)
score = 0


while True:
    score += 1
    guessing_number = input("Now start guessing: ")
    if guessing_number.isdigit():
        guessing_number = int(guessing_number)
    else:
        print("Enter a integer number next time.")
        continue

    if guessing_number == random_number:
        print("You Go it!. Just in", score, "attempt")
        break
    elif guessing_number > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

