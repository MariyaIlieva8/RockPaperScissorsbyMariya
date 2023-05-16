from random import randint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Chose [r]ock, [p]aper or [s]cissors.")

if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random = randint(1, 3)


if computer_random == 1:
    computer_random = rock
    print("The computer choose Rock.")
elif computer_random == 2:
    computer_random = scissors
    print("The computer choose Scissors.")
elif computer_random == 3:
    computer_random = paper
    print("The computer choose Paper.")

if (player_move == rock and computer_random == scissors) or (player_move == scissors and computer_random == paper) \
        or (player_move == paper and computer_random == rock):
    print("You win!")
elif player_move == computer_random:
    print("Draw!")
else:
    print("You lose.")
