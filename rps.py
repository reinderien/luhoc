from random import randint

elements = ["Paper","Rock","Scissors"]
#print(elements)

computer = elements[randint(0,2)]
#print(computer)

player = raw_input("Your choice: Rock, Paper or Scissorsn\n")
#print(player)

if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "Paper":
    if computer == "Scissors":
        print("You lose!", computer, "cut", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spelling!")

print("Game over")
