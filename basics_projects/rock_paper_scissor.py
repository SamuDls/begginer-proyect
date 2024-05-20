import random

player_score = 0
computer_score = 0

options = ["rock", "paper", "scissor"]

while True:
    print("Welcome to the rock, paper, scissors game, you must to write 'rock', 'paper' or 'scissor' to chose your play. Or 'q' to quit")
    user_option = input("Chose your option: ").lower()

    if user_option == "q":
        break

    if user_option not in options:
        print("Spell a right option please")
        continue

    random_number = random.randint(0,2)
    computer_option = options[random_number]

    if user_option == computer_option:
        print("Tie!, you choose " + user_option + "and computer option was " + computer_option)
    elif user_option == "rock" and computer_option == "scissor":
        print("You won!")
        player_score += 1
    elif user_option == "paper" and computer_option == "rock":
        print("You won!")
        player_score += 1
    elif user_option == "scissor" and computer_option == "paper":
        print("You won!")
        player_score += 1
    else:
        print("Sorry you lose")
        computer_score += 1

    
    print(f"""
          Final Score:
          Player: {player_score}
          Computer {computer_score}
          """)



