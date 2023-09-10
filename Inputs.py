import sys
import random 
from enum import Enum
#Use caps to set constant Numbers that do not change
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print(" ")
playerChoice = input("Enter a value .... \n 1 for Rock \n 2 for Paper \n 3 for Scissors\n\n")

# Convert player's value to integer
player = int(playerChoice)


if player < 1 or player > 3 :
    sys.exit("You must enter 1,2 or 3")


computerChoice = random.choice("123")

computer = int(computerChoice)

print(" ")
print("You selected " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python selected " + str(RPS(computer)).replace('RPS.', '') + ".")
print(" ")

if player == 1 and computer == 3 :
    print("🏆 You have won")
elif player == 2 and computer == 1 :
    print("🎉 You have won")
elif player == 3 and computer == 2 :
    print("😍 Player has won") 
elif player == computer :
    print("🤝It is a tie game try again")
else :
    print("🐍 Python has won")


