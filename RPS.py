# building Game rock paper scissor.
# on the way learning input and control flow.

# importing necessary module
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


player_choice = input(
    'Enter...\n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')

# casting player_choice to int value.
player = int(player_choice)

# To make sure no other no is choosen apart from 1 to 3 only.
if player < 1 | player > 3:
    sys.exit('You must enter 1, 2, or 3.')

# computer random choice
computer_choice = random.choice("123")

# casting computer choice to int type only.
computer = int(computer_choice)

# displaying.

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

# logic of the game

if player == 1 and computer == 3:
    print("🎉 You win!")

elif player == 2 and computer == 1:
    print("🎉 You win!")

elif player == 3 and computer == 2:
    print("🎉 You win!")

elif player == computer:
    print("😲 Tie game!")

else:
    print("🐍 python won !")
